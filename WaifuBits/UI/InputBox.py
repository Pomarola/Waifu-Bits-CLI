import urwid

class InputBox:
    def __init__(self):
        self._label = urwid.Text("")
        self._edit = urwid.Edit("")
        edit_attr = urwid.AttrMap(self._edit, None)

        input_columns = urwid.Columns([
            ('fixed', 3, self._label),
            edit_attr
        ])

        padded = urwid.Padding(input_columns, left=1, right=1)
        filled = urwid.Filler(padded, valign='top', top=1)
        linebox = urwid.LineBox(filled, title="INPUT NEW HABIT", title_align="left")
        self.view = urwid.AttrMap(linebox, 'bg')

    def get_text(self):
        return self._edit.edit_text.strip()

    def _reset(self):
        self._edit.edit_text = ""

    def _refresh(self, focused: bool):
        self._label.set_text(">>" if focused else "")
        self.view.set_attr_map({None: 'input_focus'} if focused else {None: None})

    def set_focus(self, focused: bool):
        self._reset()
        self._refresh(focused)
