tasks = []
while True:
    print("\nWelcome to Your To-Do List!")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("hoose an option (1-4): ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}") 

    elif choice == "2":

        new_task = input("Enter your new task: ")
        tasks.append(new_task)
        print(f"'{new_task}' has been added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("Which task number do you want to remove?")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"'{removed}' was removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                    print("Please enter a valid number.")
            
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. please choose 1, 2,3 or 4.")
                