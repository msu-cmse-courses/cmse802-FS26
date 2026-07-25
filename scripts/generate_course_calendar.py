#!/usr/bin/env python3
"""Generate an iCalendar (.ics) file from _data/schedule.yml.

This script is intentionally dependency-light and only requires PyYAML.
It supports timed class events and all-day non-class events.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def parse_hhmm(value: str) -> tuple[int, int]:
    hour_str, minute_str = value.split(":", 1)
    hour = int(hour_str)
    minute = int(minute_str)
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError(f"Invalid time: {value}")
    return hour, minute


def normalize_baseurl(baseurl: str | None) -> str:
    if not baseurl:
        return ""
    base = baseurl.strip()
    if not base:
        return ""
    if not base.startswith("/"):
        base = f"/{base}"
    return base.rstrip("/")


def combine_url(site_url: str | None, baseurl: str, event_url: str | None) -> str | None:
    if not event_url:
        return None

    suffix = event_url.strip()
    if not suffix:
        return None
    if not suffix.startswith("/"):
        suffix = f"/{suffix}"

    path = f"{baseurl}{suffix}"

    if site_url and site_url.strip():
        origin = site_url.strip().rstrip("/")
        return f"{origin}{path}"

    return path


def escape_ical_text(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def fold_ical_line(line: str, max_len: int = 75) -> list[str]:
    if len(line) <= max_len:
        return [line]

    chunks: list[str] = []
    remaining = line
    while len(remaining) > max_len:
        chunks.append(remaining[:max_len])
        remaining = " " + remaining[max_len:]
    chunks.append(remaining)
    return chunks


def format_date(value: str) -> dt.date:
    return dt.datetime.strptime(value, "%Y-%m-%d").date()


def uid_for_event(item: dict[str, Any]) -> str:
    key = "|".join(
        [
            str(item.get("date", "")),
            str(item.get("title", "")),
            str(item.get("event_type", "")),
            str(item.get("url", "")),
        ]
    )
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()
    return f"{digest}@course-website-template"


def build_event_lines(
    item: dict[str, Any],
    class_start: tuple[int, int],
    class_end: tuple[int, int],
    full_url: str | None,
    dtstamp: str,
) -> list[str]:
    event_date = format_date(str(item["date"]))
    title = str(item.get("title") or "TBD")
    event_type = str(item.get("event_type") or "class")
    day_id = item.get("day_id")

    description_parts = []
    if day_id:
        description_parts.append(f"Course day: {day_id}")
    if full_url:
        description_parts.append(f"Details: {full_url}")
    description = "\\n".join(description_parts)

    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid_for_event(item)}",
        f"DTSTAMP:{dtstamp}",
        f"SUMMARY:{escape_ical_text(title)}",
    ]

    if event_type == "class":
        start_dt = dt.datetime.combine(event_date, dt.time(class_start[0], class_start[1]))
        end_dt = dt.datetime.combine(event_date, dt.time(class_end[0], class_end[1]))
        lines.append(f"DTSTART:{start_dt.strftime('%Y%m%dT%H%M%S')}")
        lines.append(f"DTEND:{end_dt.strftime('%Y%m%dT%H%M%S')}")
    else:
        next_day = event_date + dt.timedelta(days=1)
        lines.append(f"DTSTART;VALUE=DATE:{event_date.strftime('%Y%m%d')}")
        lines.append(f"DTEND;VALUE=DATE:{next_day.strftime('%Y%m%d')}")

    if description:
        lines.append(f"DESCRIPTION:{escape_ical_text(description)}")
    if full_url:
        lines.append(f"URL:{escape_ical_text(full_url)}")

    lines.append("END:VEVENT")
    return lines


def generate_ics(
    schedule_data_path: Path,
    config_path: Path,
    output_path: Path,
    calendar_name: str,
    class_start: tuple[int, int],
    class_end: tuple[int, int],
    site_url: str | None,
    include_non_class: bool,
) -> None:
    schedule = load_yaml(schedule_data_path) or []
    config = load_yaml(config_path) or {}

    baseurl = normalize_baseurl(str(config.get("baseurl", "")))
    now_utc = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    lines: list[str] = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        "PRODID:-//Course Website Template//Schedule Calendar//EN",
        f"X-WR-CALNAME:{escape_ical_text(calendar_name)}",
    ]

    for item in schedule:
        if not isinstance(item, dict):
            continue
        if not item.get("date"):
            continue

        event_type = str(item.get("event_type") or "class")
        if event_type != "class" and not include_non_class:
            continue

        full_url = combine_url(site_url, baseurl, item.get("url"))
        event_lines = build_event_lines(item, class_start, class_end, full_url, now_utc)
        lines.extend(event_lines)

    lines.append("END:VCALENDAR")

    folded: list[str] = []
    for line in lines:
        folded.extend(fold_ical_line(line))

    output_path.write_text("\r\n".join(folded) + "\r\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate course_calendar.ics from _data/schedule.yml")
    parser.add_argument("--schedule-data", default="_data/schedule.yml", help="Path to generated schedule YAML")
    parser.add_argument("--config", default="_config.yml", help="Path to Jekyll config YAML")
    parser.add_argument("--output", default="course_calendar.ics", help="Output .ics file path")
    parser.add_argument("--calendar-name", default="Course Calendar", help="Calendar display name")
    parser.add_argument("--class-start", default="12:30", help="Class start time (HH:MM)")
    parser.add_argument("--class-end", default="13:40", help="Class end time (HH:MM)")
    parser.add_argument(
        "--site-url",
        default="",
        help="Optional absolute site URL, e.g., https://example.github.io/repo",
    )
    parser.add_argument(
        "--class-only",
        action="store_true",
        help="Include only class events and exclude non-class calendar events",
    )

    args = parser.parse_args()

    class_start = parse_hhmm(args.class_start)
    class_end = parse_hhmm(args.class_end)

    generate_ics(
        schedule_data_path=Path(args.schedule_data),
        config_path=Path(args.config),
        output_path=Path(args.output),
        calendar_name=args.calendar_name,
        class_start=class_start,
        class_end=class_end,
        site_url=args.site_url,
        include_non_class=not args.class_only,
    )

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
