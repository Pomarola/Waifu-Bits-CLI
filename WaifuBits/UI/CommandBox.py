import urwid

class CommandBox:
    def __init__(self):
        commands = [
            "↑ / ↓    --->   NAVIGATE HABIT LIST",
            "ENTER    --->   CHANGE HABIT STATUS/ADD HABIT",
            "R        --->   REMOVE HABIT",
            "N        --->   INPUT NEW HABIT",
            "ESCAPE   --->   QUIT INPUT MODE",
            "Q        --->   QUIT (IF YOU DARE WEAKLING)",
        ]

        command_list = urwid.ListBox(urwid.SimpleFocusListWalker([
            urwid.AttrMap(urwid.Text(""), 'dim'),
            *[urwid.AttrMap(urwid.Text(f"• {cmd}"), 'command') for cmd in commands]
        ]))

        padded = urwid.Padding(command_list, left=1, right=1)
        self.view = urwid.LineBox(padded, title="COMMANDS")