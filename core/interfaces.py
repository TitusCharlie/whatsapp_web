from abc import ABC, abstractmethod
from core.models import Task

class ExecutorInterface(ABC):
    """
    Abstract base class for all task executors (group messages, status uploads, etc).
    """

    @abstractmethod
    def execute(self, task: Task, profile: str):
        """
        Execute the given task using the specified WhatsApp profile.
        """
        pass