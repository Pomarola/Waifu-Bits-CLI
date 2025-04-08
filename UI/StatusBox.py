import urwid

class StatusBox:
    def __init__(self):
        content = urwid.Filler(
            urwid.AttrMap(
                urwid.Text("[ Completion info placeholder ]", align='center'),
                'dim'
            )
        )
        padded = urwid.Padding(content, left=1, right=1)
        self.widget = urwid.AttrMap(
            urwid.LineBox(padded, title="STATUS"),
            'bg'
        )

    def widget_view(self):
        return self.widget
