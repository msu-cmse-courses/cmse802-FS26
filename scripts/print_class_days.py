#!/usr/bin/env python3
"""Print all class meeting dates for the semester, skipping holidays and breaks."""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CALENDAR_PATH = ROOT / "config" / "fall_calendar.yml"


def load_calendar(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def iter_dates(start: datetime, end: datetime):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def is_on_break(day: datetime, calendar: dict) -> bool:
    for info in (calendar.get("breaks") or {}).values():
        if "date" in info:
            if day == datetime.strptime(info["date"], "%Y-%m-%d"):
                return True
        elif "start" in info and "end" in info:
            start = datetime.strptime(info["start"], "%Y-%m-%d")
            end = datetime.strptime(info["end"], "%Y-%m-%d")
            if start <= day <= end:
                return True

    for cancelled in (calendar.get("schedule_adjustments", {})
        .get("cancelled_classes", [])):
        cancelled_date = datetime.strptime(cancelled["date"], "%Y-%m-%d")
        if cancelled_date == day:
            return True

    return False


def format_day_label(day_name: str) -> str:
    labels = {
        "Monday": "Mon",
        "Tuesday": "Tues",
        "Wednesday": "Wed",
        "Thursday": "Thurs",
        "Friday": "Fri",
        "Saturday": "Sat",
        "Sunday": "Sun",
    }
    return labels.get(day_name, day_name[:3])


def main() -> None:
    calendar = load_calendar(CALENDAR_PATH)
    semester = calendar.get("semester_info", {})
    meeting_days = set(semester.get("meeting_days") or calendar.get("class_days") or [])
    start = datetime.strptime(semester["first_day"], "%Y-%m-%d")
    end = datetime.strptime(semester["last_day"], "%Y-%m-%d")

    for day in iter_dates(start, end):
        if day.strftime("%A") in meeting_days and not is_on_break(day, calendar):
            print(f"{format_day_label(day.strftime('%A'))} {day.strftime('%m/%d')}")


if __name__ == "__main__":
    main()
