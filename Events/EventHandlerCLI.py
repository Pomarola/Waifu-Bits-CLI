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
        self.selected_index = max(0, self.selected_index - 1)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def move_down(self):
        self.selected_index = min(len(self.habits) - 1, self.selected_index + 1)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def invert_status(self):
        habit = self.habits[self.selected_index]
        current_status = self.status_db.statuses.get(habit, False)
        self.status_db.update_status(habit, not current_status)
        self.ui_builder.refresh(self.habits, self.status_db.statuses, self.selected_index)

    def quit(self):
        raise urwid.ExitMainLoop()