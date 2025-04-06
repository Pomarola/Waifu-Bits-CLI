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
    def quit(self):
        pass
