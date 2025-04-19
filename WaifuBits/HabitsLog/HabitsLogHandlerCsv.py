import csv
from typing import Dict, Tuple
from datetime import date, datetime
from pathlib import Path
from ..HabitsLog.IHabitsLogHandler import IHabitsLogHandler


class HabitsLogHandlerCsv(IHabitsLogHandler):
    FIELDNAMES = ['day', 'habit', 'done']

    def __init__(self, filepath: str, day: date, log_callback=None):
        self._filepath = filepath
        self._day = day
        self._log_callback = log_callback
        self._all_statuses = {}
        self._load_all_statuses()

    def _log(self, message: str) -> None:
        if self._log_callback:
            self._log_callback(message)

    def _load_all_statuses(self) -> None:
        if not Path(self._filepath).exists():
            self._log(f"Couldn't find the file {self._filepath}. Created a new one so you can start with your journey.")
            return

        with open(self._filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                habit, day_str = row['habit'], row['day']
                day = datetime.fromisoformat(day_str).date()
                status = row['done'].lower() == 'true'
                self._all_statuses[(habit, day)] = status

    def update_status(self, habit: str, status: bool) -> None:
        self._all_statuses[(habit, self._day)] = status
        self._save_statuses()
        self._log(f"Updated status for {habit.upper()} to {'FACILITO' if status else 'RIP'}.")

    def _save_statuses(self) -> None:
        records = [
            {'day': day.isoformat(), 'habit': habit, 'done': str(done)}
            for (habit, day), done in self._all_statuses.items()
        ]

        with open(self._filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)

    def get_today_statuses(self) -> Dict[str, bool]:
        return {
            habit: done
            for (habit, day), done in self._all_statuses.items()
            if day == self._day
        }

    def get_all_statuses(self) -> Dict[Tuple[str, date], bool]:
        return self._all_statuses