import json
import os
import time
from datetime import datetime
from xml.etree.ElementTree import tostring


def list_tasks():

    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)

        for task in tasks:

            created_at = task['created_at']
            dt_obj_crt = datetime.fromisoformat(created_at)
            created_at_formated = dt_obj_crt.strftime('%Y-%m-%d %H:%M:%S')

            updated_at = task['updated_at']
            dt_obj_update = datetime.fromisoformat(updated_at)
            updated_at_formated = dt_obj_update.strftime('%Y-%m-%d %H:%M:%S')

            print(f"{task['id']} {task['description']} {task['status']} {created_at_formated} {updated_at_formated}")
    else:
        print("No tasks found")