from datetime import datetime
import uuid
import json

"""
A console edition of a todo-list/task-keeper application for the
Code-in-Place final project. 
"""
tasks = []
completed_tasks = []


def add_task():
    """
    This method gets the task to be tracked from the user and adds it to the 'database'.
    It prompts the user for various input and adds each task accordingly to the database.
    """
    new_task = {}
    print("==================================================")
    print("Hey there, what are we getting done this time? ")
    print("==================================================")
    print("Follow the prompts below to get your task inputed.")
    print("==================================================")
    id = str(uuid.uuid4())
    task_name = input("Enter the task's name: ")
    description = input("Enter the task's description: ")
    due_date = input("When do you intend on completing this (yyyy-mm-dd)? ")
    tag_number = int(input("Give it a unique tag number to help with identifying it (must be a digit): "))
    completed = False
    date_created = str(datetime.utcnow())
    new_task["id"] = id
    new_task["task_name"] = task_name
    new_task["description"] = description
    new_task["due_date"] = due_date
    new_task["date_created"] = date_created
    new_task["tag_number"] = tag_number
    new_task["completed"] = completed
    tasks.append(new_task)
    print("\nTask added successfully, you can view it now.")
    pass


def delete_task():
    """
    This method helps with deleting invalid tasks from the database.
    It prompts the user for the tag number of the task to be deleted and deletes 
    such task from the database.
    """
    tag = int(input('Please input the tag number of the task you will like to delete: '))
    for elem in tasks:
        if elem['tag_number'] == tag:
            tasks.remove(elem)


def view_pending_tasks():
    """
    This method shows all task in the database in a visually appealing manner.
    Whenever this function is called, it displays pending tasks in a visually appealing and 
    ordered manner.
    """
    if not tasks:
        print("No tasks available. Enjoy!")
    print("=======================================================")
    print("Below are your pending tasks")
    print("=======================================================")
    for index, elem in enumerate(tasks):
        print(f'Task {index + 1}')
        print(f"Task Name: {elem['task_name']}")
        print(f"Description: {elem['description']}")
        print(f"Due Date: {elem['due_date']}")
        print(f"Date Created: {elem['date_created']}")
        print(f"Tag Number: {elem['tag_number']}")
        print(f"Status: {'Completed' if elem['completed'] else 'Incomplete'}")
        print('#####################################################')
        print('#####################################################')
        print('#####################################################')
        print()
        print()


def mark_as_completed():
    """
    A function that helps with marking a task as complete.
    It prompts the user for the task tag number and helps them mark that task as complete
    """
    tag = int(input('Please input the tag number of the task you will like to mark as completed: '))
    for elem in tasks:
        if elem['tag_number'] == tag:
            if elem['completed'] == True:
                print("Task has been completed already. ")
            else:
                elem['completed'] = True
                completed_tasks.append(elem)
                tasks.remove(elem)
                print("Task has been marked as comoleted, you can find it amongst your completed tasks now. ")


def view_completed_tasks():
    """
    A function that helps with showing completed tasks.
    Whenever this function is called, it displays the tasks completed in a visually appealing and 
    ordered manner.
    """
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
        print(f"Status: {'Completed' if elem['completed'] else 'incomplete'}")
        print('###################################################')
        print('###################################################')
        print('###################################################')
        print()
        print()


def save_progress():
    progress = {
        "pending_tasks" : tasks,
        "completed_tasks" : completed_tasks
    }
    with open('data_file.json', 'w', encoding='utf-8') as data_file:
        json.dump(progress, data_file)

    




def main():
    """
    Main program that handles control flow and takes
    input from the user on the action to be take.
    """
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Remove Task")
        print("6. Save Progress")
        print("7. Exit")
        choice = int(input("Enter your choice (1-7):  "))
        match choice:
            case 1:
                add_task()
            case 2:
                mark_as_completed()
            case 3:
                view_pending_tasks()
            case 4:
                view_completed_tasks()
            case 5:
                delete_task()
            case 6:
                save_progress()
            case 7:
                print("Goodbye!")
                break
            case _:
                print("Invalid Choice")



if __name__ == '__main__':
    main()