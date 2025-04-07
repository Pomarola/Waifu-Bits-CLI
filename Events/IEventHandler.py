from abc import ABC, abstractmethod

class IEventHandler(ABC):

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def invert_status(self):
        pass

    @abstractmethod
    def remove_habit(self):
        pass

    @abstractmethod
    def enter_input_mode(self):
        pass

    @abstractmethod
    def cancel_input_mode(self):
        pass

    @abstractmethod
    def add_new_habit(self):
        pass

    @abstractmethod
    def quit(self):
        pass
