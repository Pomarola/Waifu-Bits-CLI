import urwid
from datetime import date, datetime, timedelta

class HeatMapBox:
    def __init__(self, day):
        heatmap_widget = urwid.Text("", align='left')
        filled = urwid.Filler(urwid.AttrMap(heatmap_widget, 'header'), valign='top')
        self.view = urwid.AttrMap(urwid.LineBox(filled, title="HEATMAP (LAST 31 DAYS)"), 'bg')
        self._day = day

    def set_data(self, habits: list[str], statuses: dict[tuple[str, date], bool]):
        rows = []

        # Add header with column labels -30 to 0
        header_cells = [urwid.Text("".ljust(10))]  # left label cell
        header_cells += [urwid.Text(f"{i:>2}") for i in range(-30, 1)]
        rows.append(urwid.Columns(header_cells, dividechars=0))

        for habit in habits:
            label_widget = urwid.Text(habit.upper().ljust(10))
            row = []
            for i in range(30, -1, -1):
                day = self._day - timedelta(days=i)
                row.append(urwid.AttrMap(
                    urwid.Text("  "),
                    'box_done' if statuses.get((habit, day), False) else 'box_empty'
                ))
            row_widget = urwid.Columns([label_widget] + row, dividechars=0)
            rows.append(row_widget)

        listbox = urwid.ListBox(urwid.SimpleListWalker(rows))
        self.view.original_widget = urwid.LineBox(listbox, title="HEATMAP (LAST 31 DAYS)")