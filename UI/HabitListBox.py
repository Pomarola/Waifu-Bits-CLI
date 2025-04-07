import urwid

class HabitListBox:
    def __init__(self, habits, statuses, selected_index=0):
        self.habits = habits
        self.statuses = statuses
        self.selected_index = selected_index
        self.list_walker = urwid.SimpleFocusListWalker([])
        self.widget = urwid.ListBox(self.list_walker)
        self.refresh()

    def refresh(self):
        self.list_walker.clear()
        if not self.habits:
            self.list_walker.append(urwid.Text("No habits. Press 'n' to add one."))
        else:
            for idx, habit in enumerate(self.habits):
                selected = (idx == self.selected_index)
                status_str = '[ + ]' if self.statuses.get(habit, False) else '[ - ]'
                selector = '>>' if selected else '  '
                label = f"{selector} {habit.upper():<25} {status_str}"
                text = urwid.Text(label)
                self.list_walker.append(urwid.AttrMap(text, 'reversed' if selected else None))

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
