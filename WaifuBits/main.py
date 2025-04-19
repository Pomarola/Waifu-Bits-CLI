#!/usr/bin/env python3
from dotenv import load_dotenv

import urwid
from .Configs.ConfigEnv import get_config, get_palette
from .Events.EventHandlerCLI import EventHandlerCLI
from .HabitsDb.HabitsDbHandlerTxt import HabitsDbHandlerTxt
from .HabitsLog.HabitsLogHandlerCsv import HabitsLogHandlerCsv
from .KeyHandlers.KeystrokeHandlerUrwid import KeystrokeHandlerUrwid
from .UI.HabitAppUI import HabitAppUI

def main():
    load_dotenv()
    config = get_config()

    app_ui = HabitAppUI(config["DATE"])
    habits_db = HabitsDbHandlerTxt(config["HABITS_FILEPATH"], log_callback=app_ui.log_message)
    status_db = HabitsLogHandlerCsv(config["HABIT_STATUS_FILEPATH"], config["DATE"], log_callback=app_ui.log_message)
    event_handler = EventHandlerCLI(habits_db, status_db, app_ui)

    loop = urwid.MainLoop(app_ui.view, get_palette())
    keystroke_handler = KeystrokeHandlerUrwid(loop, event_handler)
    keystroke_handler.start_listening()
    loop.run()

if __name__ == '__main__':
    main()