import json
import os
import time
from datetime import datetime
from xml.etree.ElementTree import tostring


def list_tasks(status_to_search):

    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)

        for task in tasks:
            if status_to_search is None:
                 created_at = task['created_at']
                 dt_obj_crt = datetime.fromisoformat(created_at)
                 created_at_formated = dt_obj_crt.strftime('%Y-%m-%d %H:%M:%S')

                 updated_at = task['updated_at']
                 dt_obj_update = datetime.fromisoformat(updated_at)
                 updated_at_formated = dt_obj_update.strftime('%Y-%m-%d %H:%M:%S')

                 print(f"{task['id']} {task['description']} {task['status']} {created_at_formated} {updated_at_formated}")

            elif status_to_search == 'done':
                if task['status'] == 'done':
                    created_at = task['created_at']
                    dt_obj_crt = datetime.fromisoformat(created_at)
                    created_at_formated = dt_obj_crt.strftime('%Y-%m-%d %H:%M:%S')

                    updated_at = task['updated_at']
                    dt_obj_update = datetime.fromisoformat(updated_at)
                    updated_at_formated = dt_obj_update.strftime('%Y-%m-%d %H:%M:%S')

                    print(f"{task['id']} {task['description']} {task['status']} {created_at_formated} {updated_at_formated}")

            elif status_to_search == 'todo':
                if task['status'] == 'todo':
                    created_at = task['created_at']
                    dt_obj_crt = datetime.fromisoformat(created_at)
                    created_at_formated = dt_obj_crt.strftime('%Y-%m-%d %H:%M:%S')

                    updated_at = task['updated_at']
                    dt_obj_update = datetime.fromisoformat(updated_at)
                    updated_at_formated = dt_obj_update.strftime('%Y-%m-%d %H:%M:%S')

                    print(f"{task['id']} {task['description']} {task['status']} {created_at_formated} {updated_at_formated}")

            elif status_to_search == 'in-progress':
               if task['status'] == 'in progress':
                    created_at = task['created_at']
                    dt_obj_crt = datetime.fromisoformat(created_at)
                    created_at_formated = dt_obj_crt.strftime('%Y-%m-%d %H:%M:%S')

                    updated_at = task['updated_at']
                    dt_obj_update = datetime.fromisoformat(updated_at)
                    updated_at_formated = dt_obj_update.strftime('%Y-%m-%d %H:%M:%S')

                    print(f"{task['id']} {task['description']} {task['status']} {created_at_formated} {updated_at_formated}")
            else:
                print("No task whit sutch status exists")
    else:
        print("No tasks found. make some tasks")
