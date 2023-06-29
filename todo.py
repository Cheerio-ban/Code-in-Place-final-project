from datetime import datetime
import uuid
"""
A console edition of a todo-list/task-keeper application for the
Code-in-Place final project. 
"""
tasks = []
completed_tasks = []


def add_task():
    new_task = {}
    print("==================================================")
    print("Hey there, what are we getting done this time? ")
    print("==================================================")
    print("Follow the prompts below to get your task inputed.")
    print("==================================================")
    id = uuid.uuid4()
    task_name = input("Enter the task's name: ")
    description = input("Enter the task's description: ")
    due_date = input("When do you intend on completing this? (yyyy-mm-dd) ")
    tag_number = int(input("Give it a unique tag number to help with identifying it (must be a digit) "))
    completed = False
    date_created = datetime.utcnow()
    new_task["id"] = id
    new_task["task_name"] = task_name
    new_task["description"] = description
    new_task["due_date"] = due_date
    new_task["date_created"] = date_created
    new_task["tag_number"] = tag_number
    new_task["completed"] = completed
    tasks.append(new_task)
    print("Task added successfully, you can view it now.")
    pass


def delete_task():
    tag = int(input('Please input the tag number of the task you will like to delete: '))
    for elem in tasks:
        if elem['tag_number'] == tag:
            tasks.remove(elem)


def view_tasks():
    if not tasks:
        print("No tasks available. Enjoy!")
    print("=======================================================")
    print("Below are your completed tasks")
    print("=======================================================")
    for index, elem in enumerate(tasks):
        print(f'Task {index + 1}')
        print(f"Task Name: {elem['task_name']}")
        print(f"Description: {elem['description']}")
        print(f"Due Date: {elem['due_date']}")
        print(f"Date Created: {elem['date_created']}")
        print(f"Tag Number: {elem['tag_number']}")
        print(f"Status: {elem['completed']}")
        print('###################################')
        print('###################################')
        print('###################################')
        print()
        print()


def mark_as_completed():
    tag = int(input('Please input the tag number of the task you will like to mark as completed: '))
    for elem in tasks:
        if elem['tag_number'] == tag:
            elem['completed'] = True
            completed_tasks.append(elem)
            tasks.remove(elem)


def view_completed_tasks():
    if not completed_tasks and tasks:
        print("You haven't completed your tasks yet, get to work!")
    if not completed_tasks:
        print("it's quiet here. No completed tasks.")
    print("=======================================================")
    print("Below are your completed tasks")
    print("=======================================================")
    for index, elem in enumerate(completed_tasks):
        print(f'Task {index + 1}')
        print(f"Task Name: {elem['task_name']}")
        print(f"Description: {elem['description']}")
        print(f"Due Date: {elem['due_date']}")
        print(f"Date Created: {elem['date_created']}")
        print(f"Tag Number: {elem['tag_number']}")
        print(f"Status: {elem['completed']}")
        print('###################################')
        print('###################################')
        print('###################################')
        print()
        print()


def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. View Completed Tasks")
        print("5. Remove Task")
        print("6. Exit")
        choice = int(input("Enter your choice (1-5):  "))
        match choice:
            case 1:
                add_task()
            case 2:
                delete_task()
            case 3:
                view_tasks()
            case 4:
                view_completed_tasks()
            case 5:
                delete_task()
            case 6:
                print("Goodbye!")
                break
            case _:
                print("Invalid Choice")



if __name__ == '__main__':
    main()