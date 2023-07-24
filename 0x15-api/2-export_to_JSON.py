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


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        completed_tasks = [task for task in todo_data if task['completed']]
        done_count = len(completed_tasks)
        total_count = len(todo_data)

        print(f"Employee {employee_name} tasks({done_count}/{total_count}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

        # Export to JSON
        filename = f"{employee_id}.json"
        tasks_json = [{"task": task['title'], "completed": task['completed'],
                       "username": employee_name}
                      for task in completed_tasks]

        with open(filename, 'w') as json_file:
            json.dump({f"{employee_id}": tasks_json}, json_file)

        print(f"Data exported to {filename} successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Please provide a valid integer as the employee ID.")
