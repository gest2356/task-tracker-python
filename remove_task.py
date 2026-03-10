import json
import os.path


def remove_task(task_id_to_remove):
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                tasks = [tasks]

        task_to_finish = next((t for t in tasks if t['id'] == task_id_to_remove), None)

        if task_to_finish:
            tasks.remove(task_to_finish)
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f, indent=4)

        else:
            print(f"No task with id {task_id_to_remove} was found.")
    else:
        print("No tasks found. make some tasks")
