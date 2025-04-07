import urwid
from UI.IUIBuilder import IUIBuilder

class UIBuilderCLI(IUIBuilder):
    def __init__(self):
        self.list_walker = None
        self.habit_widgets = []
        self.list_box = None
        self.view = None
        self.footer = None

    def build_ui(self, habits, statuses, selected_index=0, footer=None):
        self.footer = footer
        self.habit_widgets = [
            self._create_habit_widget(habit, statuses.get(habit, False), idx == selected_index)
            for idx, habit in enumerate(habits)
        ]

        self.list_walker = urwid.SimpleFocusListWalker(self.habit_widgets)
        self.list_box = urwid.ListBox(self.list_walker)

        self.view = urwid.Frame(
            self.list_box,
            header=urwid.Text("📅 Habit Tracker (↑↓ Enter r n q)"),
            footer=self.footer
        )

        return self.view

    def refresh(self, habits, statuses, selected_index, footer=None):
        self.footer = footer
        self.list_walker.clear()

        if not habits:
            placeholder = urwid.Text("No habits available. Press 'n' to add one, or 'q' to quit.", align='center')
            self.list_walker.append(urwid.AttrMap(placeholder, None))
        else:
            for idx, habit in enumerate(habits):
                widget = self._create_habit_widget(habit, statuses.get(habit, False), idx == selected_index)
                self.list_walker.append(widget)

            self.list_box.set_focus(selected_index)

        self.view.footer = self.footer

    @staticmethod
    def _create_habit_widget(habit, status, is_selected):
        selector = '>>' if is_selected else '  '
        status_symbol = '[ + ]' if status else '[ - ]'
        habit_text = f"{selector} {habit:<25} {status_symbol}"

        txt_widget = urwid.Text(habit_text, align='left')
        return urwid.AttrMap(urwid.Padding(txt_widget, left=1, right=1), 'reversed' if is_selected else None)
