#!/usr/bin/python3
"""
REST API to return information about
TODO list progress
based on given employee ID
"""
import requests
import sys


def get_employee_info(employee_id):
    """
    This helps to get information about
    TODO list progress based on
    employee ID given.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        response = requests.get(user_url)
        response.raise_for_status()
        user_data = response.json()

        name = user_data.get('name')

        response = requests.get(todo_url)
        response.raise_for_status()
        todo_data = response.json()

        done_tasks = [task['title'] for task in todo_data if task['completed']]
        done_count = len(done_tasks)
        total_count = len(todo_data)

        print(f"Employee {name} is done with tasks({done_count}/{total_count}):")
        for task in done_tasks:
            print(f"\t {task}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
