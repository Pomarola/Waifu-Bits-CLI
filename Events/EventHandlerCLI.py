import urwid

from Events.IEventHandler import IEventHandler

class EventHandlerCLI(IEventHandler):
    def __init__(self, habits_db, status_db, ui):
        self.habits_db = habits_db
        self.status_db = status_db
        self.ui = ui
        self._refresh_ui()

    def move_up(self):
        self.ui.move_up_list()

    def move_down(self):
        self.ui.move_down_list()

    def _refresh_ui(self):
        self.ui.refresh(self.habits_db.get_habits(), self.status_db.get_today_statuses(), self.status_db.get_all_statuses())

    def invert_status(self):
        name = self.ui.get_selected_habit()
        if name:
            current = self.status_db.get_today_statuses().get(name, False)
            self.status_db.update_status(name, not current)
            self._refresh_ui()

    def remove_habit(self):
        name = self.ui.get_selected_habit()
        if name:
            self.habits_db.remove_habit(name)
            self._refresh_ui()

    def enter_input_mode(self):
        self.ui.focus_input()

    def cancel_input_mode(self):
        self.ui.focus_list()

    def add_new_habit(self):
        name = self.ui.get_input_text()
        if name:
            self.habits_db.add_habit(name)
            self._refresh_ui()
        self.ui.focus_list()

    def quit(self):
        raise urwid.ExitMainLoop()