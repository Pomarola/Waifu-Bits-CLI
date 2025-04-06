from abc import ABC, abstractmethod
from typing import List, Dict

class IUIBuilder(ABC):

    @abstractmethod
    def build_ui(self, habits: List[str], statuses: Dict[str, bool]):
        pass

    @abstractmethod
    def refresh(self, habits: List[str], statuses: Dict[str, bool], selected_index: int):
        pass
