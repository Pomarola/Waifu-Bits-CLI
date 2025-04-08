import urwid

class StatusBox:
    def __init__(self):
        content = urwid.Filler(urwid.Text("[ Completion info placeholder ]", align='center'))
        padded = urwid.Padding(content, left=1, right=1)
        self.widget = urwid.LineBox(padded, title="STATUS")

    def widget_view(self):
        return self.widget
