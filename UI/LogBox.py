import urwid

class LogBox:
    def __init__(self):
        self._messages = []
        self._list_walker = urwid.SimpleFocusListWalker([])
        listbox = urwid.ListBox(self._list_walker)
        padded_text = urwid.Padding(listbox, left=1, right=1)
        self.view = urwid.LineBox(padded_text, title="RECENT LOGS", title_align='left')

    def add_message(self, message: str):
        self._messages.append(message)
        self._messages = self._messages[-4:]  # Keep last 4 messages
        self._render_messages()

    def _render_messages(self):
        self._list_walker.clear()
        self._list_walker.append(urwid.AttrMap(urwid.Text(""), 'log'))  # padding

        for i, msg in enumerate(reversed(self._messages)):
            style = 'log_focus' if i == 0 else 'log_unfocus'
            prefix = "> " if i == 0 else "  "
            self._list_walker.append(urwid.AttrMap(urwid.Text(prefix + msg), style))