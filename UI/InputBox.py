import urwid

class InputBox:
    def __init__(self):
        self.edit = urwid.Edit("")
        self.attr = urwid.AttrMap(self.edit, None)
        padded = urwid.Padding(self.attr, left=1, right=1)
        filled = urwid.Filler(padded, valign='top', top=1)
        self.widget = urwid.LineBox(filled, title="INPUT NEW HABIT", title_align="left")

    def reset(self):
        self.edit.edit_text = ""

    def get_text(self):
        return self.edit.edit_text.strip()

    def widget_view(self):
        return self.widget

    def focus(self):
        self.attr.set_attr_map({None: 'input_focus'})

    def unfocus(self):
        self.attr.set_attr_map({None: None})
