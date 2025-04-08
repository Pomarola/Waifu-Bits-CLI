#!/usr/bin/env python3
from dotenv import load_dotenv

import urwid
from Configs.ConfigEnv import get_config, get_palette
from Events.EventHandlerCLI import EventHandlerCLI
from HabitsDb.HabitsDbHandlerTxt import HabitsDbHandlerTxt
from HabitsLog.HabitsLogHandlerCsv import HabitsLogHandlerCsv
from KeyHandlers.KeystrokeHandlerUrwid import KeystrokeHandlerUrwid
from UI.CommandBox import CommandBox
from UI.HabitAppUI import HabitAppUI
from UI.HabitListBox import HabitListBox
from UI.HeaderBox import HeaderBox
from UI.InputBox import InputBox
from UI.LogBox import LogBox
from UI.StatusBox import StatusBox


def main():
    load_dotenv()

    config = get_config()

    log_box = LogBox()

    def log_message(msg):
        log_box.add_message(msg)

    habits_db = HabitsDbHandlerTxt(config["HABITS_FILEPATH"], log_callback=log_message)
    status_db = HabitsLogHandlerCsv(config["HABIT_STATUS_FILEPATH"], config["DATE"], log_callback=log_message)

    header = HeaderBox()
    list_box = HabitListBox(habits_db.get_habits(), status_db.statuses)
    status_box = StatusBox()
    input_box = InputBox()
    command_box = CommandBox()

    app_ui = HabitAppUI(header, list_box, status_box, input_box, command_box, log_box)

    loop = urwid.MainLoop(app_ui.widget_view(), get_palette())
    event_handler = EventHandlerCLI(habits_db, status_db, list_box, input_box, app_ui, loop)
    keystroke_handler = KeystrokeHandlerUrwid(loop, event_handler)
    keystroke_handler.start_listening()

    loop.run()

if __name__ == '__main__':
    main()