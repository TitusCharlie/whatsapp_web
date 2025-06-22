import json
from pathlib import Path
from typing import List
from core.models import Task

TASKS_FILE = Path("tasks.json")


class TaskRepository:
    @staticmethod
    def load_tasks() -> List[Task]:
        """
        Load tasks from the tasks.json file.
        """
        if not TASKS_FILE.exists():
            return []

        try:
            with open(TASKS_FILE, "r") as f:
                raw_tasks = json.load(f)
                return [Task(**t) for t in raw_tasks]
        except json.JSONDecodeError:
            print("⚠️ Failed to decode tasks.json — starting fresh.")
            return []

    @staticmethod
    def save_tasks(tasks: List[Task]) -> None:
        """
        Save a list of Task objects to tasks.json.
        """
        with open(TASKS_FILE, "w") as f:
            json.dump([t.__dict__ for t in tasks], f, indent=2)