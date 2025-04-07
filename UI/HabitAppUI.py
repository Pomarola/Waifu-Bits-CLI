import urwid

class FixedFocusPile(urwid.Pile):
    def __init__(self, contents, ui):
        self.ui = ui  # reference to HabitAppUI
        super().__init__(contents)

    def keypress(self, size, key):
        # Only allow focus switch to input box if we're in input mode
        if self.ui.focus_mode == 'input':
            return super().keypress(size, key)
        else:
            # Block focus movement between widgets
            if key in ('up', 'down'):
                return self.contents[0][0].keypress(size, key)
            return super().keypress(size, key)

class HabitAppUI:
    def __init__(self, habit_list_box, new_input_box):
        self.habit_list_box = habit_list_box
        self.new_input_box = new_input_box
        self.focus_mode = 'list'

        self.pile = FixedFocusPile([
            ('weight', 2, self.habit_list_box.widget_view()),
            ('weight', 1, self.new_input_box.widget_view())
        ], self)

        self.view = urwid.Frame(self.pile, header=urwid.Text("📅 Habit Tracker (↑↓ Enter r n q)"))

    def widget_view(self):
        return self.view

    def is_list_focused(self):
        return self.focus_mode == 'list'

    def focus(self, mode: str):
        self.focus_mode = mode
        if mode == 'list':
            self.pile.set_focus(0)
            self.habit_list_box.focus()
            self.new_input_box.unfocus()
        elif mode == 'input':
            self.pile.set_focus(1)
            self.habit_list_box.unfocus()
            self.new_input_box.focus()
