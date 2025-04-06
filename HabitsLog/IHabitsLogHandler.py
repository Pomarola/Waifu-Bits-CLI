from abc import ABC, abstractmethod
from typing import Dict

class IHabitsLogHandler(ABC):

    @abstractmethod
    def get_statuses(self) -> Dict[str, bool]:
        """Get all habit statuses."""
        pass

    @abstractmethod
    def update_status(self, habit: str, status: bool) -> None:
        """Update or create the habit status."""
        pass