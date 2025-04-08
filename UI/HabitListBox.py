import urwid

class HabitListBox:
    def __init__(self, habits, statuses, selected_index=0):
        self.habits = habits
        self.statuses = statuses
        self.selected_index = selected_index
        self.focused = True  # Track focus state
        self.list_walker = urwid.SimpleFocusListWalker([])
        listbox = urwid.ListBox(self.list_walker)
        padded = urwid.Padding(listbox, left=1, right=1)
        self.widget = urwid.LineBox(padded, title="HABIT LIST")
        self.refresh()

    def refresh(self):
        self.list_walker.clear()
        if not self.habits:
            self.list_walker.append(urwid.Text("Bro you have no habits, what are you doing? Do me a favor and press 'N' "))
        else:
            for idx, habit in enumerate(self.habits):
                selected = (idx == self.selected_index) and self.focused
                status_str = '[ + ]' if self.statuses.get(habit, False) else '[ - ]'
                selector = '>>' if selected else '  '

                text = urwid.Columns([
                    ('weight', 1, urwid.Text(f"{selector} {habit.upper():<40}")),
                    (len(status_str), urwid.Text(status_str, align='right'))
                ])

                self.list_walker.append(
                    urwid.AttrMap(text, 'reversed' if selected else None)
                )

    def widget_view(self):
        return self.widget

    def move_up(self):
        if self.habits:
            self.selected_index = (self.selected_index - 1) % len(self.habits)
            self.refresh()

    def move_down(self):
        if self.habits:
            self.selected_index = (self.selected_index + 1) % len(self.habits)
            self.refresh()

    def get_selected(self):
        if self.habits:
            return self.habits[self.selected_index]
        return None

    def set_data(self, habits, statuses):
        self.habits = habits
        self.statuses = statuses
        self.refresh()

    def focus(self):
        self.focused = True
        self.refresh()

    def unfocus(self):
        self.focused = False
        self.refresh()
