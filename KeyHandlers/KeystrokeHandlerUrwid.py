from KeyHandlers.IKeystrokeHandler import IKeystrokeHandler

class KeystrokeHandlerUrwid(IKeystrokeHandler):
    def __init__(self, loop, event_handler):
        self.loop = loop
        self.event_handler = event_handler

    def start_listening(self):
        def handle_input(key):
            if key == 'up':
                self.event_handler.move_up()
            elif key == 'down':
                self.event_handler.move_down()
            elif key == 'enter':
                self.event_handler.invert_status()
            elif key.lower() == 'r':
                self.event_handler.remove_habit()
            elif key.lower() == 'q':
                self.event_handler.quit()

        self.loop.unhandled_input = handle_input