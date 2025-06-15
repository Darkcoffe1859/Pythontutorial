import json

# File to store tasks
FILENAME = "tasks.json"

#task list
tasks = []

#Load tasks from file (if file exists)

def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open(FILENAME, "w")as f:
        json.dump(tasks, f)

def add_task(task):
    tasks.append({"task": task, "done": False})
    save_tasks()
    return f"Task added: {task}"

def view_tasks():
    if not tasks:
        print("No tasks added yet. ")
    else:
        print("Your Tasks:")
        for i, task in enumerates(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()
            print(f"Task removed: {removed['task']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

# Function to mark task as done

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = true
            save_tasks()
            print(f"Task marked as done: {tasks[task_num - 1]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Function to show the menu

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")


# Start by loading tasks from file

load_tasks()

#main Program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        new_task = input("Enter a task to add: ")
        print(add_task(new_task))
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Pleaser enter 1-5.")