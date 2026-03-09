import argparse
import json

from put_task_in_progress import put_task_in_progress

from task import Task
from add_task import add_task
from list_tasks import list_tasks
from finish_task import finish_task
from remove_task import remove_task

#new_task = Task(1, "nice")
#new_task2 = Task(2, "", "ds")

#text = json.dumps(new_task.get_json_string())
#print(text)

#new_task3 = Task.from_json(json.loads(text))
#print(new_task3)

def main():
    parser = argparse.ArgumentParser(prog='task-tracker', description='Task Tracker project from roadmap.sh')

    subparsers = parser.add_subparsers(dest="command", help='sub-command help')

    add_parser = subparsers.add_parser('add', help='add a new task')
    add_parser.add_argument("description", type=str, help="Text input for the task")

    list_parser = subparsers.add_parser('list', help='list all tasks')

    edit_parser = subparsers.add_parser('mark-done', help='finish a task')
    edit_parser.add_argument("task_id_to_edit", type=int, help="Text input for the task")

    edit_parser = subparsers.add_parser('mark-in-progress', help='finish a task')
    edit_parser.add_argument("task_id_to_edit", type=int, help="Text input for the task")

    remove_parser = subparsers.add_parser('remove', help='delete a task')
    remove_parser.add_argument("task_id_to_delete", type=int, help="Text input for the task")

    args = parser.parse_args()

    if args.command == 'add':
        print(f"Add a new task: {args.description}")
        add_task(args.description)

    elif args.command == 'list':
        list_tasks()

    elif args.command == 'mark-done':
        finish_task(args.task_id_to_edit)

    elif args.command == 'mark-in-progress':
        put_task_in_progress(args.task_id_to_edit)

    elif args.command == 'remove':
        remove_task(args.task_id_to_delete)

if __name__ == '__main__':
    main()