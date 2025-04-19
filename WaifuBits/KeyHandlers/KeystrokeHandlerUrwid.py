from ..KeyHandlers.IKeystrokeHandler import IKeystrokeHandler

class KeystrokeHandlerUrwid(IKeystrokeHandler):
    def __init__(self, loop, event_handler):
        self.loop = loop
        self.event_handler = event_handler

    def start_listening(self):
        def handle_input(key):
            if isinstance(key, tuple):
                return  # Ignore mouse or unsupported events

            if self.event_handler.ui.is_input_focused():
                if key == 'enter':
                    self.event_handler.add_new_habit()
                elif key == 'esc':
                    self.event_handler.cancel_input_mode()

            else:
                if key == 'up':
                    self.event_handler.move_up()
                elif key == 'down':
                    self.event_handler.move_down()
                elif key == 'enter':
                    self.event_handler.invert_status()
                elif key.lower() in ('r', 'backspace', 'delete'):
                    self.event_handler.remove_habit()
                elif key.lower() == 'n':
                    self.event_handler.enter_input_mode()
                elif key.lower() in ('q', 'esc'):
                    self.event_handler.quit()

        self.loop.unhandled_input = handle_input