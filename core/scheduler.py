import threading
import time
from .repository import TaskRepository
from core.executors import GroupMessageExecutor, StatusUploadExecutor

class TaskScheduler:
    EXECUTOR_MAP = {
        "message": GroupMessageExecutor(),
        "status": StatusUploadExecutor(),
    }

    @classmethod
    def run(cls):
        def worker():
            while True:
                tasks = TaskRepository.load_tasks()
                for task in tasks:
                    if task.is_due() and task.status == "pending":
                        for profile in task.profiles:
                            executor = cls.EXECUTOR_MAP.get(task.type)
                            if executor:
                                try:
                                    threading.Thread(
                                        target=executor.execute,
                                        args=(task, profile),
                                        daemon=True
                                    ).start()
                                    task.status = "completed"
                                    task.executed_at = time.strftime("%Y-%m-%d %H:%M")
                                except Exception as e:
                                    print(f"[{profile}] Failed:", e)
                                    task.status = "failed"
                TaskRepository.save_tasks(tasks)
                time.sleep(60)  # check every minute

        threading.Thread(target=worker, daemon=True).start()