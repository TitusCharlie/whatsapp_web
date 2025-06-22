from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a scheduled WhatsApp task.
    """

    def __init__(
        self,
        id: str,
        type: str,
        profiles: List[str],
        target: str,
        content: Optional[str],
        media_path: Optional[str],
        scheduled_for: str,
    ):
        self.id = id
        self.type = type  # "group_message" or "status_upload"
        self.profiles = profiles
        self.target = target
        self.content = content
        self.media_path = media_path
        self.scheduled_for = scheduled_for  # Expected format: "YYYY-MM-DD HH:MM"

    def is_due(self) -> bool:
        """
        Checks if the task's scheduled time has passed.
        """
        try:
            scheduled_dt = datetime.strptime(self.scheduled_for, "%Y-%m-%d %H:%M")
            return datetime.now() >= scheduled_dt
        except ValueError:
            return False