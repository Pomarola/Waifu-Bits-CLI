import urwid
from datetime import date, datetime, timedelta

class HeatMapBox:
    def __init__(self, day):
        heatmap_widget = urwid.Text("", align='left')
        filled = urwid.Filler(urwid.AttrMap(heatmap_widget, 'header'), valign='top')
        self.view = urwid.AttrMap(urwid.LineBox(filled, title="MONTHLY HEATMAP"), 'bg')
        self._day = day

    def set_data(self, habits: list[str], statuses: dict[tuple[str, date], bool]):
        rows = []

        # Add header with column labels -30 to 0
        header_cells = [('fixed', 30, urwid.Text(""))]
        header_cells += [
            ('fixed', 4, urwid.Text(f"{i}".center(3))) for i in range(-30, 1)
        ]
        rows.append(urwid.Divider())
        rows.append(urwid.Columns(header_cells, dividechars=1))

        for habit in habits:
            label_widget = urwid.Padding(urwid.Text(habit.upper(), wrap='clip'), left=5, right=0)
            row = []
            for i in range(30, -1, -1):
                day = self._day - timedelta(days=i)
                is_done = statuses.get((habit, day), False)
                text = "██" if is_done else " "
                row.append(urwid.AttrMap(
                    urwid.Padding(urwid.Text(text, align='center'), left=0, right=0),
                    'box_done' if is_done else 'box_empty'
                ))
            row_widget = urwid.Columns([('fixed', 30, label_widget)] + [('fixed', 4, cell) for cell in row], dividechars=1)
            rows.append(row_widget)

        listbox = urwid.ListBox(urwid.SimpleListWalker(rows))
        self.view.original_widget = urwid.LineBox(listbox, title="MONTHLY HEATMAP")