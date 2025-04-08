import urwid

class LogBox:
    def __init__(self):
        self.messages = []
        self.list_walker = urwid.SimpleFocusListWalker([])
        listbox = urwid.ListBox(self.list_walker)
        padded_text = urwid.Padding(listbox, left=1, right=1)
        self.widget = urwid.LineBox(padded_text, title="RECENT LOGS", title_align='left')

    def add_message(self, message: str):
        self.messages.append(message)
        self.messages = self.messages[-4:]  # Keep last 4 messages

        self.list_walker.clear()
        self.list_walker.append(urwid.AttrMap(urwid.Text(""), 'log'))  # wide space to blend in

        for i, msg in enumerate(reversed(self.messages)):
            style = 'log_focus' if i == 0 else 'log_unfocus'
            prefix = "> " if i == 0 else "  "
            self.list_walker.append(urwid.AttrMap(urwid.Text(prefix + msg), style))

    def widget_view(self):
        return self.widget
