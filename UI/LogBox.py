import urwid

class LogBox:
    def __init__(self):
        self.messages = []
        self.text_widget = urwid.Text("", align='left')
        padded_text = urwid.Padding(self.text_widget, left=1, right=1)
        self.widget = urwid.LineBox(padded_text, title="RECENT LOGS", title_align='left')

    def add_message(self, message: str):
        self.messages.append(message)
        self.messages = self.messages[-4:]  # Keep last 5 messages

        formatted = [""]  # Padding from title
        for i, msg in enumerate(reversed(self.messages)):
            if i == 0:
                formatted.append(f"> {msg}")
            else:
                formatted.append(f"  {msg}")
        self.text_widget.set_text("\n".join(formatted))

    def widget_view(self):
        return self.widget
