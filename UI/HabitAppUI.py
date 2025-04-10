from _datetime import date
from typing import Tuple

import urwid

from UI.CommandBox import CommandBox
from UI.HabitListBox import HabitListBox
from UI.HeatMapBox import HeatMapBox
from UI.InputBox import InputBox
from UI.LogBox import LogBox
from UI.StatusBox import StatusBox


class FixedFocusPile(urwid.Pile):
    def __init__(self, contents, ui):
        self.ui = ui  # reference to HabitAppUI
        super().__init__(contents)

    def keypress(self, size, key):
        if self.ui._focus_mode == 'input':
            bottom_columns = self.contents[1][0]  # bottom columns (commands + right pile)
            right_pile = bottom_columns.contents[1][0]  # right pile (input + log)
            input_widget = right_pile.contents[0][0]
            return input_widget.keypress(size, key)

        # Forward keys to top section (habit list + status)
        top_columns = self.contents[0][0]
        habit_widget = top_columns.contents[0][0]
        return habit_widget.keypress(size, key)

class HabitAppUI:
    def __init__(self, day):
        self._heat_map_box = HeatMapBox(day)
        self._habit_box = HabitListBox()
        self._status_box = StatusBox()
        self._input_box = InputBox()
        self._command_box = CommandBox()
        self._log_box = LogBox()

        # Compose layout
        self.pile = FixedFocusPile([
            ('weight', 5, urwid.Columns([
                ('weight', 1, urwid.AttrMap(self._habit_box.view, 'bg')),
                ('weight', 3, urwid.Pile([
                    ('weight', 1, urwid.AttrMap(self._heat_map_box.view, 'header')),
                    ('weight', 1, urwid.AttrMap(self._status_box.view, 'dim'))
                ]))
            ])),
            ('weight', 1, urwid.Columns([
                ('weight', 1, urwid.AttrMap(self._command_box.view, 'bg')),
                ('weight', 3, urwid.Pile([
                    ('weight', 1, urwid.AttrMap(self._input_box.view, 'input')),
                    ('weight', 3, urwid.AttrMap(self._log_box.view, 'log'))
                ]))
            ]))
        ], self)

        self.view = urwid.Frame(self.pile)
        self._focus_mode = 'list'  # Default focus mode
        self.focus_list()

    def is_input_focused(self):
        return self._focus_mode == 'input'

    def log_message(self, message: str):
        self._log_box.add_message(message)

    def focus_list(self):
        self._focus_mode = 'list'
        self.pile.focus = 0
        self._habit_box.set_focus(True)
        self._input_box.set_focus(False)

    def focus_input(self):
        self._focus_mode = 'input'
        self.pile.focus = 1
        self._habit_box.set_focus(False)
        self._input_box.set_focus(True)

    def move_up_list(self):
        self._habit_box.move_up()

    def move_down_list(self):
        self._habit_box.move_down()

    def get_selected_habit(self):
        return self._habit_box.get_selected()

    def get_input_text(self):
        return self._input_box.get_text()

    def refresh(self, habits: list[str], today_statuses: dict[str, bool], all_statuses: dict[Tuple[str, date], bool]):
        self._habit_box.set_data(habits, today_statuses)
        self._status_box.set_data(habits, today_statuses)
        self._heat_map_box.set_data(habits, all_statuses)

