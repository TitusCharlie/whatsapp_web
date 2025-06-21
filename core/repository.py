import json
from pathlib import Path
from core.models import Task

TASKS_FILE = Path("tasks.json")

class TaskRepository:
    @staticmethod
    def load_tasks():
        if not TASKS_FILE.exists():
            return []
        with open(TASKS_FILE, "r") as f:
            raw_tasks = json.load(f)
            return [Task(**t) for t in raw_tasks]

    @staticmethod
    def save_tasks(tasks):
        with open(TASKS_FILE, "w") as f:
            json.dump([t.__dict__ for t in tasks], f, indent=2)