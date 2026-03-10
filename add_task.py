import json
import os

from task import Task


def add_task(task_description):

    if os.path.exists("./tasks.json"):
        try:
            with open("./tasks.json", "r") as read_file:
                tasks = json.load(read_file)
                if not isinstance(tasks, list):
                    tasks = [tasks]
        except FileNotFoundError:
            tasks = []

        new_task = Task(len(tasks) + 1,task_description)

        tasks.append(new_task.get_json_string())

        with open("./tasks.json", "w") as whrite_file:
            json.dump(tasks, whrite_file, indent=4)
    else:
        tasks = []
        new_task = Task(1 , task_description)
        tasks.append(new_task.get_json_string())
        with open("./tasks.json", "w") as whrite_file:
            json.dump(tasks, whrite_file, indent=4)

    return f"task added: {task_description}"





