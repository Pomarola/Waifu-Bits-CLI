import urwid
from ..UI.WaifuText import waifu_nino, arara_nino, happy_nino, curious_nino, mad_nino, angry_nino

class CuteAnimeGirlBox:
    def __init__(self):
        self.view = urwid.AttrMap(
            urwid.LineBox(urwid.Padding(urwid.Text("", align='left'), left=1, right=1), title="WAIF-U-METER"),
            'bg'
        )

    def set_data(self, habits, statuses):
        relevant_statuses = {habit: statuses.get(habit, False) for habit in habits}
        completion_rate = (
            sum(relevant_statuses.values()) / len(relevant_statuses)
            if relevant_statuses else 0
        )

        if completion_rate >= 1:
            art = waifu_nino()
        elif completion_rate >= 0.8:
            art = arara_nino()
        elif completion_rate >= 0.6:
            art = happy_nino()
        elif completion_rate >= 0.4:
            art = curious_nino()
        elif completion_rate >= 0.2:
            art = mad_nino()
        else:
            art = angry_nino()

        new_content = urwid.Filler(
            urwid.AttrMap(
                urwid.Text(art.lstrip('\n'), align='center', wrap='clip'),
                'bg'
            )
        )
        padded = urwid.Padding(new_content, left=1, right=1)
        self.view.original_widget = urwid.LineBox(padded, title="WAIF-U-METER")