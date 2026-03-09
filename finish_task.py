import json

def finish_task(task_to_be_done_id):
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        if not isinstance(tasks, list):
            tasks = [tasks]

    task_to_finish = next((t for t in tasks if t['id'] == task_to_be_done_id), None)

    if task_to_finish:
        task_to_finish['status'] = "done"
        tasks.sort(key=lambda task: task['id'])
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)
    else:
        print(f"No task with id {task_to_be_done_id} was found.")






