#!/usr/bin/env python3
"""Build website schedule metadata from the course calendar and source markdown files.

This module acts as the bridge between the course calendar and the markdown pages in
`Schedule/`. It reads the semester calendar, infers the scheduled dates from the
filename convention used by class pages, and emits the YAML data later consumed by the
site templates.

Single source of truth:
- config/[semester]_calendar.yml (dates and semester adjustments)
- Schedule/*.md (class pages and relative events)
"""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

import yaml


VALID_WEEKDAYS = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}


@dataclass(frozen=True)
class ParsedScheduleFilename:
    """A schedule markdown file translated into its date relationship metadata."""

    file_path: Path
    anchor_day: int
    relation: str
    offset_days: int | None = None
    weekday: str | None = None


@dataclass(frozen=True)
class ScheduleFilenameWarning:
    """A filename pattern issue that should be surfaced in generated warnings output."""

    file_path: Path
    message: str


def _front_matter_data(file_path: Path) -> dict:
    """Return YAML front matter for a markdown file as a dictionary, if present."""

    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}

    frontmatter_lines: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        frontmatter_lines.append(line)

    if not frontmatter_lines:
        return {}

    frontmatter_text = "\n".join(frontmatter_lines)
    parsed = yaml.safe_load(frontmatter_text) or {}
    return parsed if isinstance(parsed, dict) else {}


def _should_publish_schedule_item(file_path: Path) -> bool:
    """Whether a schedule item should remain clickable in generated schedule data.

    Files that set `publish: false` are still kept in the repository but are treated as
    hidden schedule entries. They can still appear in the generated calendar title list
    without a URL when that is useful for staging future assignments.
    """

    frontmatter = _front_matter_data(file_path)
    publish_value = frontmatter.get("publish", frontmatter.get("published"))

    if publish_value is None:
        return True
    if isinstance(publish_value, bool):
        return publish_value
    if isinstance(publish_value, str):
        normalized = publish_value.strip().lower()
        return normalized not in {"false", "no", "0", "off"}
    return bool(publish_value)


def parse_schedule_filename(file_path: Path) -> tuple[ParsedScheduleFilename | None, ScheduleFilenameWarning | None]:
    """Parse one Schedule filename using the instructor convention."""

    stem = file_path.stem.strip().lower()

    class_match = re.match(r"^(\d{2})-class-[a-z0-9][a-z0-9-]*$", stem)
    if class_match:
        return ParsedScheduleFilename(file_path=file_path, anchor_day=int(class_match.group(1)), relation="class"), None

    same_match = re.match(r"^(\d{2})-same-[a-z0-9][a-z0-9-]*$", stem)
    if same_match:
        return ParsedScheduleFilename(file_path=file_path, anchor_day=int(same_match.group(1)), relation="same"), None

    plus_match = re.match(r"^(\d{2})-plus-(\d+)-[a-z0-9][a-z0-9-]*$", stem)
    if plus_match:
        return (
            ParsedScheduleFilename(
                file_path=file_path,
                anchor_day=int(plus_match.group(1)),
                relation="plus",
                offset_days=int(plus_match.group(2)),
            ),
            None,
        )

    next_match = re.match(r"^(\d{2})-next-([a-z]{3})-[a-z0-9][a-z0-9-]*$", stem)
    if next_match:
        weekday = next_match.group(2)
        if weekday not in VALID_WEEKDAYS:
            return None, ScheduleFilenameWarning(file_path=file_path, message=f"Invalid weekday token: {weekday}")
        return (
            ParsedScheduleFilename(
                file_path=file_path,
                anchor_day=int(next_match.group(1)),
                relation="next",
                weekday=weekday,
            ),
            None,
        )

    return None, ScheduleFilenameWarning(
        file_path=file_path,
        message=(
            "Filename does not match convention. Expected one of: "
            "NN-class-*, NN-same-*, NN-plus-D-*, NN-next-WDAY-*"
        ),
    )


def parse_schedule_directory(schedule_dir: Path) -> tuple[list[ParsedScheduleFilename], list[ScheduleFilenameWarning]]:
    """List valid schedule files and any filename-level warnings in a directory."""

    parsed: list[ParsedScheduleFilename] = []
    warnings: list[ScheduleFilenameWarning] = []

    for file_path in sorted(schedule_dir.glob("*.md")):
        item, warning = parse_schedule_filename(file_path)
        if item is not None:
            parsed.append(item)
        elif warning is not None:
            warnings.append(warning)

    return parsed, warnings


def markdown_title_for_file(file_path: Path) -> str:
    """Extract a human-readable title from markdown content."""

    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            match = re.match(r"^\s*title\s*:\s*[\"']?(.*?)[\"']?\s*$", line)
            if match and match.group(1).strip():
                return match.group(1).strip()

    for line in lines:
        heading = line.strip()
        if heading.startswith("# "):
            return heading[2:].strip()

    return "TBD"


class ScheduleUpdater:
    """Populate schedule metadata from the calendar and markdown schedule definitions."""

    def __init__(self, calendar_path: str):
        """Load the semester calendar used to anchor class-date calculations."""

        with open(calendar_path, "r", encoding="utf-8") as handle:
            self.calendar = yaml.safe_load(handle) or {}

    def _resolve_target_date(self, item: ParsedScheduleFilename, class_dates: list[datetime]) -> datetime:
        """Translate a parsed filename relation into the actual target class date."""

        anchor_date = class_dates[item.anchor_day - 1]
        if item.relation == "same":
            return anchor_date
        if item.relation == "plus":
            return anchor_date + timedelta(days=int(item.offset_days or 0))
        if item.relation == "next":
            return self._next_weekday_after(anchor_date, item.weekday)
        if item.relation == "class":
            return anchor_date
        raise ValueError(f"Unsupported schedule relation: {item.relation}")

    def update_schedule_page_dates(self, schedule_dir: Path) -> None:
        """Ensure every schedule markdown file has a current front-matter date."""

        parsed_items, _ = parse_schedule_directory(schedule_dir)
        class_dates = self._meeting_dates()

        for item in parsed_items:
            target_date = self._resolve_target_date(item, class_dates)
            file_path = item.file_path
            text = file_path.read_text(encoding="utf-8")
            lines = text.splitlines()

            if not lines:
                continue

            target_date_text = target_date.strftime("%Y-%m-%d")

            if lines[0].strip() != "---":
                text = "---\nlayout: schedule\ndate: " + target_date_text + "\n---\n\n" + text
                file_path.write_text(text, encoding="utf-8")
                continue

            end_index = None
            for index in range(1, len(lines)):
                if lines[index].strip() == "---":
                    end_index = index
                    break

            if end_index is None:
                continue

            frontmatter_lines = lines[1:end_index]
            body_lines = lines[end_index + 1 :]
            frontmatter_text = "\n".join(frontmatter_lines)
            frontmatter_data = yaml.safe_load(frontmatter_text) or {}
            if not isinstance(frontmatter_data, dict):
                frontmatter_data = {}

            existing_date = frontmatter_data.get("date")
            if existing_date is not None and str(existing_date).strip() == target_date_text:
                continue

            frontmatter_data["date"] = target_date_text
            new_frontmatter = yaml.safe_dump(frontmatter_data, sort_keys=False, allow_unicode=False).rstrip()
            body_text = "\n".join(body_lines)
            updated_text = "---\n" + new_frontmatter + "\n---\n"
            if body_text:
                updated_text += "\n" + body_text
            file_path.write_text(updated_text, encoding="utf-8")

    def _first_day(self) -> datetime:
        """Return the first date in the semester calendar."""

        return datetime.strptime(self.calendar["semester_info"]["first_day"], "%Y-%m-%d")

    def _last_day(self) -> datetime:
        """Return the final date in the semester calendar."""

        return datetime.strptime(self.calendar["semester_info"]["last_day"], "%Y-%m-%d")

    def _meeting_days(self) -> list[str]:
        """Return the weekday names on which classes normally meet."""

        semester_days = self.calendar.get("semester_info", {}).get("meeting_days")
        class_days = self.calendar.get("class_days")
        return list(semester_days or class_days or ["Tuesday", "Thursday"])

    def _break_ranges(self) -> list[tuple[datetime, datetime]]:
        """Collect the date ranges excluded from class meetings, such as breaks."""

        ranges: list[tuple[datetime, datetime]] = []

        for info in (self.calendar.get("breaks") or {}).values():
            if "date" in info:
                day = datetime.strptime(info["date"], "%Y-%m-%d")
                ranges.append((day, day))
            elif "start" in info and "end" in info:
                start = datetime.strptime(info["start"], "%Y-%m-%d")
                end = datetime.strptime(info["end"], "%Y-%m-%d")
                ranges.append((start, end))

        for cancelled_class in self.calendar.get("schedule_adjustments", {}).get("cancelled_classes", []):
            cancelled_date = datetime.strptime(cancelled_class["date"], "%Y-%m-%d")
            ranges.append((cancelled_date, cancelled_date))

        return ranges

    def _is_break(self, day: datetime) -> bool:
        """Return whether a given date falls inside a semester break or cancellation."""

        for start, end in self._break_ranges():
            if start <= day <= end:
                return True
        return False

    def _meeting_dates(self) -> list[datetime]:
        """Generate the date list for every scheduled class meeting in the semester."""

        current = self._first_day()
        last_day = self._last_day()
        meeting_days = set(self._meeting_days())

        dates: list[datetime] = []
        while current <= last_day:
            if current.strftime("%A") in meeting_days and not self._is_break(current):
                dates.append(current)
            current += timedelta(days=1)

        return dates

    @staticmethod
    def _week_start_iso_for(day: datetime) -> str:
        """Return the ISO date for the start of the week containing the supplied day."""

        return (day - timedelta(days=day.weekday())).strftime("%Y-%m-%d")

    @staticmethod
    def _next_weekday_after(day: datetime, weekday_token: str) -> datetime:
        """Return the next occurrence of a named weekday after the supplied date."""

        weekday_map = {
            "mon": 0,
            "tue": 1,
            "wed": 2,
            "thu": 3,
            "fri": 4,
            "sat": 5,
            "sun": 6,
        }
        target = weekday_map[weekday_token]
        delta = (target - day.weekday()) % 7
        if delta == 0:
            delta = 7
        return day + timedelta(days=delta)

    def _calendar_non_class_events(self) -> list[dict[str, str | None]]:
        """Return non-class semester events such as breaks or institutional calendar dates."""

        events: list[dict[str, str | None]] = []

        for break_name, info in (self.calendar.get("breaks") or {}).items():
            description = str(info.get("description") or break_name.replace("_", " ").title())

            if "date" in info:
                day = datetime.strptime(info["date"], "%Y-%m-%d")
                events.append(
                    {
                        "date": day.strftime("%Y-%m-%d"),
                        "week_start": self._week_start_iso_for(day),
                        "title": description,
                        "url": None,
                        "event_type": "non_class",
                        "day_id": None,
                    }
                )
                continue

            if "start" in info and "end" in info:
                start = datetime.strptime(info["start"], "%Y-%m-%d")
                end = datetime.strptime(info["end"], "%Y-%m-%d")
                cursor = start
                while cursor <= end:
                    events.append(
                        {
                            "date": cursor.strftime("%Y-%m-%d"),
                            "week_start": self._week_start_iso_for(cursor),
                            "title": description,
                            "url": None,
                            "event_type": "non_class",
                            "day_id": None,
                        }
                    )
                    cursor += timedelta(days=1)

        return events

    def build_schedule_events(self, schedule_dir: Path) -> tuple[list[dict[str, str | None]], list[str]]:
        """Create the schedule metadata consumed by the website templates.

        Each entry contains a title and an optional URL. Hidden items with `publish: false`
        are kept in the source tree and can still appear in the schedule list, but their URL
        is intentionally set to `None` so they do not appear clickable.
        """

        parsed_items, parse_warnings = parse_schedule_directory(schedule_dir)
        warnings: list[str] = [f"{w.file_path.name}: {w.message}" for w in parse_warnings]

        class_dates = self._meeting_dates()
        events: list[dict[str, str | None]] = []

        class_items = [item for item in parsed_items if item.relation == "class"]
        class_items.sort(key=lambda item: item.file_path.name)
        class_by_anchor: dict[int, ParsedScheduleFilename] = {}

        for item in class_items:
            if item.anchor_day in class_by_anchor:
                warnings.append(
                    f"{item.file_path.name}: duplicate class anchor {item.anchor_day:02d}; "
                    f"using {class_by_anchor[item.anchor_day].file_path.name}"
                )
                continue
            class_by_anchor[item.anchor_day] = item

        for index, class_date in enumerate(class_dates, start=1):
            class_item = class_by_anchor.get(index)
            if class_item is None:
                warnings.append(f"Day{index:02d}: missing NN-class-* file; inserted TBD entry")
                events.append(
                    {
                        "date": class_date.strftime("%Y-%m-%d"),
                        "week_start": self._week_start_iso_for(class_date),
                        "title": "TBD",
                        "url": None,
                        "event_type": "class",
                        "day_id": f"Day{index:02d}",
                    }
                )
                continue

            title = markdown_title_for_file(class_item.file_path)
            public_url = None if not _should_publish_schedule_item(class_item.file_path) else f"/Schedule/{class_item.file_path.stem}"
            events.append(
                {
                    "date": class_date.strftime("%Y-%m-%d"),
                    "week_start": self._week_start_iso_for(class_date),
                    "title": title,
                    "url": public_url,
                    "event_type": "class",
                    "day_id": f"Day{index:02d}",
                }
            )

        for item in parsed_items:
            if item.relation == "class":
                continue

            if item.anchor_day < 1 or item.anchor_day > len(class_dates):
                warnings.append(
                    f"{item.file_path.name}: anchor {item.anchor_day:02d} is out of range for this semester"
                )
                continue

            anchor_date = class_dates[item.anchor_day - 1]
            if item.relation == "same":
                target_date = anchor_date
            elif item.relation == "plus":
                target_date = anchor_date + timedelta(days=int(item.offset_days or 0))
            elif item.relation == "next":
                if not item.weekday:
                    warnings.append(f"{item.file_path.name}: missing weekday token")
                    continue
                target_date = self._next_weekday_after(anchor_date, item.weekday)
            else:
                warnings.append(f"{item.file_path.name}: unsupported relation {item.relation}")
                continue

            title = markdown_title_for_file(item.file_path)
            public_url = None if not _should_publish_schedule_item(item.file_path) else f"/Schedule/{item.file_path.stem}"
            events.append(
                {
                    "date": target_date.strftime("%Y-%m-%d"),
                    "week_start": self._week_start_iso_for(target_date),
                    "title": title,
                    "url": public_url,
                    "event_type": item.relation,
                    "day_id": f"Day{item.anchor_day:02d}",
                }
            )

        events.extend(self._calendar_non_class_events())
        events.sort(key=lambda entry: (str(entry.get("date", "")), str(entry.get("title", ""))))
        return events, warnings

    def update_schedule(
        self,
        schedule_dir: str = "Schedule",
        schedule_data_path: str = "_data/schedule.yml",
        schedule_warnings_path: str = "_data/schedule_warnings.yml",
    ) -> None:
        """Write the generated schedule YAML and warning summary for the website."""

        self.update_schedule_page_dates(Path(schedule_dir))
        events, warnings = self.build_schedule_events(Path(schedule_dir))

        schedule_data_file = Path(schedule_data_path)
        schedule_data_file.parent.mkdir(parents=True, exist_ok=True)
        schedule_data_file.write_text(
            yaml.safe_dump(events, sort_keys=False, allow_unicode=False),
            encoding="utf-8",
        )

        warning_rows = [{"warning": warning} for warning in warnings]
        warnings_file = Path(schedule_warnings_path)
        warnings_file.parent.mkdir(parents=True, exist_ok=True)
        warnings_file.write_text(
            yaml.safe_dump(warning_rows, sort_keys=False, allow_unicode=False),
            encoding="utf-8",
        )


def main() -> None:
    """Command-line entry point for generating the schedule data files."""

    parser = argparse.ArgumentParser(description="Update generated schedule data from config")
    parser.add_argument("--calendar", required=True, help="Path to semester calendar YAML file")
    parser.add_argument(
        "--schedule-dir",
        default="Schedule",
        help="Directory containing Schedule markdown files using NN-* filename convention",
    )
    parser.add_argument(
        "--schedule-data",
        default="_data/schedule.yml",
        help="Path to generated schedule YAML used by the website",
    )
    parser.add_argument(
        "--schedule-warnings",
        default="_data/schedule_warnings.yml",
        help="Path to generated warnings YAML for filename/schedule mismatches",
    )
    parser.add_argument(
        "--rendered-site-dir",
        default=None,
        help="Optional directory to receive rendered schedule markdown pages for local site builds",
    )
    args = parser.parse_args()

    updater = ScheduleUpdater(args.calendar)
    updater.update_schedule(
        schedule_dir=args.schedule_dir,
        schedule_data_path=args.schedule_data,
        schedule_warnings_path=args.schedule_warnings,
    )

    if args.rendered_site_dir:
        output_dir = Path(args.rendered_site_dir)
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        shutil.copytree(
            Path.cwd(),
            output_dir,
            ignore=shutil.ignore_patterns(
                ".git",
                ".venv",
                "_site",
                ".jekyll-cache",
                "envs",
                ".ipynb_checkpoints",
                "__pycache__",
                ".vscode",
                ".githooks",
            ),
            dirs_exist_ok=True,
        )
        print(f"Rendered schedule pages into {output_dir}.")

    print("Generated schedule data and schedule warnings.")


if __name__ == "__main__":
    main()
