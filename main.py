#!/usr/bin/env python3
from dotenv import load_dotenv

import urwid
from Configs.ConfigEnv import get_config, get_palette
from Events.EventHandlerCLI import EventHandlerCLI
from HabitsDb.HabitsDbHandlerTxt import HabitsDbHandlerTxt
from HabitsLog.HabitsLogHandlerCsv import HabitsLogHandlerCsv
from KeyHandlers.KeystrokeHandlerUrwid import KeystrokeHandlerUrwid
from UI.UIBuilderCLI import UIBuilderCLI


def main():
    load_dotenv()

    config = get_config()

    habits_db = HabitsDbHandlerTxt(config["HABITS_FILEPATH"])
    status_db = HabitsLogHandlerCsv(config["HABIT_STATUS_FILEPATH"], config["DATE"])

    ui_builder = UIBuilderCLI()
    ui = ui_builder.build_ui(habits_db.get_habits(), status_db.statuses)

    event_handler = EventHandlerCLI(habits_db, status_db, ui_builder)
    loop = urwid.MainLoop(ui, get_palette())
    keystroke_handler = KeystrokeHandlerUrwid(loop, event_handler)
    keystroke_handler.start_listening()

    loop.run()

if __name__ == '__main__':
    main()
