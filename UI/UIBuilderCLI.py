import urwid
from UI.IUIBuilder import IUIBuilder

class UIBuilderCLI(IUIBuilder):
    def __init__(self):
        self.list_walker = None
        self.habit_widgets = []
        self.list_box = None
        self.view = None

    def build_ui(self, habits, statuses, selected_index=0):
        self.habit_widgets = [
            self._create_habit_widget(habit, statuses.get(habit, False), idx == selected_index)
            for idx, habit in enumerate(habits)
        ]

        self.list_walker = urwid.SimpleFocusListWalker(self.habit_widgets)
        self.list_box = urwid.ListBox(self.list_walker)

        self.view = urwid.Frame(
            self.list_box,
            header=urwid.Text("📅 Habit Tracker (↑↓ to navigate, Enter to toggle, q to quit)")
        )

        return self.view

    def refresh(self, habits, statuses, selected_index):
        self.list_walker.clear()
        for idx, habit in enumerate(habits):
            widget = self._create_habit_widget(habit, statuses.get(habit, False), idx == selected_index)
            self.list_walker.append(widget)
        self.list_box.set_focus(selected_index)

    @staticmethod
    def _create_habit_widget(habit, status, is_selected):
        status_str = '✅' if status else '❌'
        habit_text = f"{status_str} {habit}"

        txt_widget = urwid.Text(habit_text, align='left')

        if is_selected:
            return urwid.AttrMap(urwid.Padding(txt_widget, left=1, right=1), 'reversed')
        else:
            return urwid.AttrMap(urwid.Padding(txt_widget, left=1, right=1), None)
