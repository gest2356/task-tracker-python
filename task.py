from datetime import datetime


class Task:
    def __init__(self, task_id, description, status="In progress", created_at=None, updated_at=None):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __str__(self):
        return str(self.__dict__)

    def get_json_string(self):
        return {"id": self.id, "description": self.description, "status": self.status , "created_at": self.created_at.isoformat(), "updated_at": self.updated_at.isoformat()}

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["id"], json_data["description"], json_data["status"], datetime.fromisoformat(json_data["created_at"]), datetime.fromisoformat(json_data["updated_at"]))

