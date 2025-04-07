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

        self.habits = habits_db.get_habits()
        self.selected_index = 0
        self.refresh()

    def refresh(self):
        self.habits = self.habits_db.get_habits()
        self.list_box.set_data(self.habits, self.status_db.statuses)

    def move_up(self):
        if self.ui.focus_mode == 'list':
            self.list_box.move_up()

    def move_down(self):
        if self.ui.focus_mode == 'list':
            self.list_box.move_down()

    def invert_status(self):
        if self.ui.focus_mode == 'list':
            habit = self.list_box.get_selected()
            if habit:
                current = self.status_db.statuses.get(habit, False)
                self.status_db.update_status(habit, not current)
                self.refresh()

    def remove_habit(self):
        if self.ui.focus_mode == 'list':
            habit = self.list_box.get_selected()
            if habit:
                self.habits_db.remove_habit(habit)
                self.refresh()

    def enter_input_mode(self):
        self.ui.focus_input()
        self.input_box.reset()

    def cancel_input_mode(self):
        self.ui.focus_list()

    def add_new_habit(self):
        name = self.input_box.get_text()
        if name:
            self.habits_db.add_habit(name)
        self.refresh()
        self.ui.focus_list()

    def quit(self):
        raise urwid.ExitMainLoop()