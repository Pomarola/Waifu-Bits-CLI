import urwid

from Events.IEventHandler import IEventHandler

class EventHandlerCLI(IEventHandler):
    def __init__(self, habits_db, status_db, ui_builder):
        self.habits_db = habits_db
        self.status_db = status_db
        self.ui_builder = ui_builder
        self.habits = self.habits_db.get_habits()
        self.selected_index = 0

    def move_up(self):
        if not self.habits:
            return
        self.selected_index = (self.selected_index - 1) % len(self.habits)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def move_down(self):
        if not self.habits:
            return
        self.selected_index = (self.selected_index + 1) % len(self.habits)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def invert_status(self):
        if not self.habits:
            return
        habit = self.habits[self.selected_index]
        current_status = self.status_db.statuses.get(habit, False)
        self.status_db.update_status(habit, not current_status)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def remove_habit(self):
        if not self.habits:
            return

        habit_to_remove = self.habits[self.selected_index]

        self.habits_db.remove_habit(habit_to_remove)
        self.habits = self.habits_db.get_habits()

        if self.selected_index >= len(self.habits):
            self.selected_index = max(0, len(self.habits) - 1)

        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def quit(self):
        raise urwid.ExitMainLoop()