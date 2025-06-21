from datetime import datetime

class Task:
    def __init__(self, id, type, profiles, target, content, media_path, scheduled_for):
        self.id = id
        self.type = type
        self.profiles = profiles
        self.target = target
        self.content = content
        self.media_path = media_path
        self.scheduled_for = scheduled_for

    def is_due(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M") >= self.scheduled_for