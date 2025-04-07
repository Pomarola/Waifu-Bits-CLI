import urwid

from Events.IEventHandler import IEventHandler

class EventHandlerCLI(IEventHandler):
    def __init__(self, habits_db, status_db, list_box, input_box, ui, loop):
        self.habits_db = habits_db
        self.status_db = status_db
        self.list_box = list_box
        self.input_box = input_box
        self.ui = ui
        self.loop = loop

        self.habits = self.habits_db.get_habits()
        self.refresh()
        self.ui.focus('list')

    def refresh(self):
        self.habits = self.habits_db.get_habits()
        self.list_box.set_data(self.habits, self.status_db.statuses)

    def move_up(self):
        if self.ui.is_list_focused():
            self.list_box.move_up()

    def move_down(self):
        if self.ui.is_list_focused():
            self.list_box.move_down()

    def invert_status(self):
        if self.ui.is_list_focused():
            habit = self.list_box.get_selected()
            if habit:
                current = self.status_db.statuses.get(habit, False)
                self.status_db.update_status(habit, not current)
                self.refresh()

    def remove_habit(self):
        if self.ui.is_list_focused():
            habit = self.list_box.get_selected()
            if habit:
                self.habits_db.remove_habit(habit)
                self.refresh()
                if self.list_box.selected_index >= len(self.habits):
                    self.list_box.selected_index = max(0, len(self.habits) - 1)
                self.list_box.refresh()

    def enter_input_mode(self):
        self.ui.focus('input')

    def cancel_input_mode(self):
        self.input_box.reset()
        self.ui.focus('list')

    def add_new_habit(self):
        name = self.input_box.get_text()
        if name:
            self.habits_db.add_habit(name)
            self.input_box.reset()
        self.refresh()
        self.ui.focus('list')


    def quit(self):
        raise urwid.ExitMainLoop()