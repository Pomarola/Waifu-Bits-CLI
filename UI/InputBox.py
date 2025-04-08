import urwid

class InputBox:
    def __init__(self):
        self.label = urwid.Text("")
        self.edit = urwid.Edit("")
        self.attr = urwid.AttrMap(self.edit, None)

        input_columns = urwid.Columns([
            ('fixed', 3, self.label),
            self.attr
        ])

        padded = urwid.Padding(input_columns, left=1, right=1)
        filled = urwid.Filler(padded, valign='top', top=1)
        self.linebox = urwid.LineBox(filled, title="INPUT NEW HABIT", title_align="left")
        self.container = urwid.AttrMap(self.linebox, 'bg')
        self.widget = self.container

    def reset(self):
        self.edit.edit_text = ""

    def get_text(self):
        return self.edit.edit_text.strip()

    def widget_view(self):
        return self.widget

    def focus(self):
        self.attr.set_attr_map({None: 'input_focus'})
        self.label.set_text(">>")
        self.container.set_attr_map({None: 'input_focus'})

    def unfocus(self):
        self.attr.set_attr_map({None: None})
        self.label.set_text("")
        self.container.set_attr_map({None: None})
