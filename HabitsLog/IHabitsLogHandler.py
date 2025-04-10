from abc import ABC, abstractmethod
from typing import Dict, Tuple
from datetime import date

class IHabitsLogHandler(ABC):

    @abstractmethod
    def get_today_statuses(self) -> Dict[str, bool]:
        """Get all habit statuses."""
        pass

    @abstractmethod
    def get_all_statuses(self) -> Dict[Tuple[str, date], bool]:
        """Get all habit statuses."""
        pass

    @abstractmethod
    def update_status(self, habit: str, status: bool) -> None:
        """Update or create the habit status."""
        pass