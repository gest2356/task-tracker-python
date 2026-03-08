import argparse
import json
from argparse import ArgumentParser

from task import Task

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

    args = parser.parse_args()

    if args.command == 'add':
        print(f"Add a new task: {args.description}")

if __name__ == '__main__':
    main()