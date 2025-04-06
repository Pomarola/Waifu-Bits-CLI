from abc import ABC, abstractmethod
from typing import List

class IHabitsDbHandler(ABC):

    @abstractmethod
    def add_habit(self, habit: str) -> None:
        """Add a new habit."""
        pass

    @abstractmethod
    def remove_habit(self, habit: str) -> None:
        """Remove an existing habit."""
        pass

    @abstractmethod
    def get_habits(self) -> List[str]:
        """Return all habits."""
        pass
