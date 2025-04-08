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
        self.linebox = urwid.LineBox(padded, title="HABIT LIST")
        self.container = urwid.AttrMap(self.linebox, None)
        self.widget = self.container
        self.refresh()

    def refresh(self):
        self.list_walker.clear()
        if not self.habits:
            empty_text = urwid.AttrMap(
                urwid.Text("Bro you have no habits, what are you doing? Do me a favor and press 'N' "),
                'dim'
            )
            self.list_walker.append(empty_text)
        else:
            for idx, habit in enumerate(self.habits):
                selected = (idx == self.selected_index) and self.focused
                status_str = '[ + ]' if self.statuses.get(habit, False) else '[ - ]'
                selector = '>>' if selected else '  '
                selector_inv = '<<' if selected else '  '

                text = urwid.Columns([
                    ('weight', 1, urwid.Text(f"{selector} {habit.upper():<35}")),
                    (len(status_str) + 3, urwid.Text(f"{status_str} {selector_inv}", align='right'))
                ])

                if selected:
                    highlight = 'selected'
                else:
                    highlight = 'unselected' if self.focused else 'bg'
                self.list_walker.append(urwid.AttrMap(text, highlight))

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
        self.container.set_attr_map({None: 'log'})
        self.refresh()

    def unfocus(self):
        self.focused = False
        self.container.set_attr_map({None: None})
        self.refresh()
