import urwid

class HeaderBox:
    def __init__(self):
        content = urwid.Filler(
            urwid.Text("[ Heatmap of last 50 days placeholder ]", align='center'),
            valign='top'
        )
        self.widget = urwid.LineBox(content, title="HEADER")

    def widget_view(self):
        return self.widget
