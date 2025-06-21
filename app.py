from flask import Flask, render_template, request, redirect
from core.models import Task
from core.repository import TaskRepository
from core.scheduler import TaskScheduler
import uuid, os
from datetime import datetime

app = Flask(__name__)

# Start the background scheduler
TaskScheduler.run()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/schedule", methods=["POST"])
def schedule():
    task_type = request.form["task_type"]
    target = request.form["target"]
    message = request.form.get("message", "")
    profiles_raw = request.form["profiles"]
    scheduled_time = request.form["scheduled_time"]
    media_path = request.form.get("media_path", "")

    # Parse and sanitize inputs
    profiles = [p.strip() for p in profiles_raw.split(",") if p.strip()]
    task_id = str(uuid.uuid4())

    new_task = Task(
        id=task_id,
        type=task_type,
        profiles=profiles,
        target=target,
        content=message,
        media_path=media_path,
        scheduled_for=scheduled_time
    )

    tasks = TaskRepository.load_tasks()
    tasks.append(new_task)
    TaskRepository.save_tasks(tasks)

    return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
