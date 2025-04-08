import os
from typing import List, Callable
from HabitsDb.IHabitsDbHandler import IHabitsDbHandler

class HabitsDbHandlerTxt(IHabitsDbHandler):
    def __init__(self, filepath: str, log_callback=None):
        self.filepath = filepath
        self._habits = self._load_habits()
        self._log_callback = log_callback

    def _load_habits(self) -> List[str]:
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def _save_habits(self) -> None:
        with open(self.filepath, 'w') as file:
            file.write('\n'.join(self._habits) + ('\n' if self._habits else ''))

    def add_habit(self, habit: str) -> None:
        normalized_habit = habit.strip().lower()
        if normalized_habit in self._habits:
            self._log_callback("Bro, you already have that habit in your list. You're COOKED")
            return  # Already exists
        if len(self._habits) >= 50:
            self._log_callback("Bro, less is more you know that right? 50 is the max, chill out")
            return
        self._habits.append(normalized_habit)
        self._save_habits()
        self._log_callback("Successfully added your new challenge: " + normalized_habit.upper())

    def remove_habit(self, habit: str) -> None:
        normalized_habit = habit.strip().lower()
        if normalized_habit in self._habits:
            self._habits.remove(normalized_habit)
            self._save_habits()
            self._log_callback("Successfully removed your weakness: " + normalized_habit.upper())

    def get_habits(self) -> List[str]:
        return self._habits.copy()  # Return a copy to avoid external modification
