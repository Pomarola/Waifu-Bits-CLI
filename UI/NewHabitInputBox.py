import urwid

class NewHabitInputBox:
    def __init__(self):
        self.edit = urwid.Edit("New Activity: ")
        self.attr = urwid.AttrMap(self.edit, None)
        self.box = urwid.Filler(self.attr)

    def reset(self):
        self.edit.edit_text = ""

    def get_text(self):
        return self.edit.edit_text.strip()

    def widget_view(self):
        return self.box

    def focus(self):
        self.attr.set_attr_map({None: 'input_focus'})

    def unfocus(self):
        self.attr.set_attr_map({None: None})
