import urwid

class NewHabitInputBox:
    def __init__(self):
        self.edit = urwid.Edit("New Activity: ")
        self.box = urwid.Filler(self.edit)

    def reset(self):
        self.edit.edit_text = ""

    def get_text(self):
        return self.edit.edit_text.strip()

    def widget_view(self):
        return self.box
