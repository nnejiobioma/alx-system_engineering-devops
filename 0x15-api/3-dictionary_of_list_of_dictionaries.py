#!/usr/bin/python3
"""
    A python script that, using a REST API, for a given
    employee ID, returns information about his/her TODO
    list progress.This extends python script to
    export data in the JSON format.
"""
import json
import requests
import sys


def get_all_employees_todo_progress():
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users'
    todo_url = f'{base_url}/todos'

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        users_data = user_response.json()

        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        all_employees_tasks = {}
        for user in users_data:
            employee_id = user['id']
            employee_name = user['name']
            employee_tasks = [task for task in todo_data if task
                              ['userId'] == employee_id]

            completed_tasks = [{'username': employee_name,
                                'task': task['title'],
                                'completed': task['completed']}
                               for task in employee_tasks]

            all_employees_tasks[employee_id] = completed_tasks

        print(f"Data collection complete.")
        # Export to JSON
        filename = "todo_all_employees.json"
        with open(filename, 'w') as json_file:
            json.dump(all_employees_tasks, json_file)

        print(f"Data exported to {filename} successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_all_employees_todo_progress()
