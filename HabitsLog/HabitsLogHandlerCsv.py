import csv
import os
from typing import Dict
from HabitsLog.IHabitsLogHandler import IHabitsLogHandler


class HabitsLogHandlerCsv(IHabitsLogHandler):
    def __init__(self, filepath: str, date: str):
        self.filepath = filepath
        self.date = date
        self.statuses = self._load_statuses()

    def _load_statuses(self) -> Dict[str, bool]:
        statuses = {}
        if not os.path.exists(self.filepath):
            return statuses

        with open(self.filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['date'] == self.date:
                    statuses[row['habit']] = row['done'].lower() == 'true'
            return statuses

    def update_status(self, habit: str, status: bool) -> None:
        self.statuses[habit] = status
        self._save_statuses()

    def _save_statuses(self) -> None:
        records = []
        # Load existing data except current date
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                records = [row for row in reader if row['date'] != self.date]

        # Add or update today's statuses
        for habit, done in self.statuses.items():
            records.append({'date': self.date, 'habit': habit, 'done': str(done)})

        # Save everything back
        with open(self.filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['date', 'habit', 'done'])
            writer.writeheader()
            writer.writerows(records)

    def get_statuses(self) -> Dict[str, bool]:
        return self.statuses
