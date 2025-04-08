import urwid

class HeaderBox:
    def __init__(self):
        content = urwid.Filler(
            urwid.AttrMap(
                urwid.Text("[ Heatmap of last 50 days placeholder ]", align='center'),
                'header'
            ),
            valign='top'
        )
        self.widget = urwid.AttrMap(
            urwid.LineBox(content, title="HEADER"),
            'bg'
        )

    def widget_view(self):
        return self.widget
