import urwid

class HabitListBox:
    def __init__(self):
        self._habits = []
        self._statuses = {}
        self._selected_index = 0
        self._focused = True  # Track focus state
        self._list_walker = urwid.SimpleFocusListWalker([])
        linebox = urwid.LineBox(urwid.Padding(urwid.ListBox(self._list_walker), left=1, right=1), title="HABIT LIST")
        self.view = urwid.AttrMap(linebox, None)

    def _render_row(self, habit, idx):
        selected = (idx == self._selected_index) and self._focused
        status_str = '[ + ]' if self._statuses.get(habit, False) else '[ - ]'
        selector = '>>' if selected else '  '
        selector_inv = '<<' if selected else '  '
        text = urwid.Columns([
            ('weight', 1, urwid.Text(f"{selector} {habit.upper():<35}")),
            (len(status_str) + 3, urwid.Text(f"{status_str} {selector_inv}", align='right'))
        ])
        highlight = 'selected' if selected else 'unselected' if self._focused else 'bg'
        return urwid.AttrMap(text, highlight)

    @staticmethod
    def _render_empty_message():
        return urwid.AttrMap(
            urwid.Text("Bro you have no habits, what are you doing?\n"
                       "Do me a favor and press 'N' ", align="center"),
            'log_focus'
        )

    def refresh(self):
        self._list_walker.clear()
        self._ensure_valid_selection()
        if not self._habits:
            self._list_walker.append(self._render_empty_message())
        else:
            for idx, habit in enumerate(self._habits):
                self._list_walker.append(self._render_row(habit, idx))

    def move_up(self):
        if self._habits:
            self._selected_index = (self._selected_index - 1) % len(self._habits)
            self.refresh()

    def move_down(self):
        if self._habits:
            self._selected_index = (self._selected_index + 1) % len(self._habits)
            self.refresh()

    def get_selected(self):
        return self._habits[self._selected_index] if self._habits else None

    def set_data(self, habits, statuses):
        self._habits = habits
        self._statuses = statuses
        self.refresh()

    def set_focus(self, focused: bool):
        self._focused = focused
        self.view.set_attr_map({None: 'log'} if focused else {None: None})
        self.refresh()

    def _ensure_valid_selection(self):
        if self._selected_index >= len(self._habits):
            self._selected_index = max(0, len(self._habits) - 1)
