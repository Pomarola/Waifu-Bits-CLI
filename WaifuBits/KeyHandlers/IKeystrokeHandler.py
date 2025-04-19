from abc import ABC, abstractmethod

class IKeystrokeHandler(ABC):

    @abstractmethod
    def start_listening(self):
        pass
