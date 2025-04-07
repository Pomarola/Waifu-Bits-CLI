#!/usr/bin/env python3
from dotenv import load_dotenv

import urwid
from Configs.ConfigEnv import get_config, get_palette
from Events.EventHandlerCLI import EventHandlerCLI
from HabitsDb.HabitsDbHandlerTxt import HabitsDbHandlerTxt
from HabitsLog.HabitsLogHandlerCsv import HabitsLogHandlerCsv
from KeyHandlers.KeystrokeHandlerUrwid import KeystrokeHandlerUrwid
from UI.HabitAppUI import HabitAppUI
from UI.HabitListBox import HabitListBox
from UI.NewHabitInputBox import NewHabitInputBox
from UI.UIBuilderCLI import UIBuilderCLI


def main():
    load_dotenv()

    config = get_config()

    habits_db = HabitsDbHandlerTxt(config["HABITS_FILEPATH"])
    status_db = HabitsLogHandlerCsv(config["HABIT_STATUS_FILEPATH"], config["DATE"])

    list_box = HabitListBox(habits_db.get_habits(), status_db.statuses)
    input_box = NewHabitInputBox()
    app_ui = HabitAppUI(list_box, input_box)

    loop = urwid.MainLoop(app_ui.widget_view(), get_palette())
    event_handler = EventHandlerCLI(habits_db, status_db, list_box, input_box, app_ui, loop)
    keystroke_handler = KeystrokeHandlerUrwid(loop, event_handler)
    keystroke_handler.start_listening()

    loop.run()

if __name__ == '__main__':
    main()