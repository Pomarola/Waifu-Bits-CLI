import urwid

class FixedFocusPile(urwid.Pile):
    def __init__(self, contents, ui):
        self.ui = ui  # reference to HabitAppUI
        super().__init__(contents)

    def keypress(self, size, key):
        if self.ui.focus_mode == 'input':
            bottom_columns = self.contents[1][0]  # bottom columns (commands + right pile)
            right_pile = bottom_columns.contents[1][0]  # right pile (input + log)
            input_widget = right_pile.contents[0][0]
            return input_widget.keypress(size, key)

        # Forward keys to top section (habit list + status)
        top_columns = self.contents[0][0]
        habit_widget = top_columns.contents[0][0]
        return habit_widget.keypress(size, key)

class HabitAppUI:
    def __init__(self, header, habit_box, status_box, input_box, command_box, log_box):
        self.header = header
        self.habit_box = habit_box
        self.status_box = status_box
        self.input_box = input_box
        self.command_box = command_box
        self.log_box = log_box

        self.focus_mode = 'list'  # 'list' or 'input'

        # Compose layout
        self.pile = FixedFocusPile([
            ('weight', 5, urwid.Columns([
                ('weight', 1, self.habit_box.widget_view()),
                ('weight', 3, urwid.Pile([
                    ('weight', 1, self.header.widget_view()),
                    ('weight', 1, self.status_box.widget_view())
                ]))
            ])),
            ('weight', 1, urwid.Columns([
                ('weight', 1, self.command_box.widget_view()),
                ('weight', 3, urwid.Pile([
                    ('weight', 1, self.input_box.widget_view()),
                    ('weight', 3, self.log_box.widget_view())
                ]))
            ]))
        ], self)

        self.view = urwid.Frame(self.pile)

    def widget_view(self):
        return self.view

    def is_list_focused(self):
        return self.focus_mode == 'list'

    def focus(self, mode: str):
        self.focus_mode = mode
        if mode == 'list':
            self.pile.set_focus(0)
            self.habit_box.focus()
            self.input_box.unfocus()
        elif mode == 'input':
            self.pile.set_focus(1)
            self.habit_box.unfocus()
            self.input_box.focus()
