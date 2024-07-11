tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def complete_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as completed.")
    else:
        print("Invalid task index.")

def remove_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        task_name = tasks[task_index]["task"]
        del tasks[task_index]
        print(f"Task '{task_name}' removed.")
    else:
        print("Invalid task index.")

def print_tasks():
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index + 1}. [{status}] {task['task']}")
    print()

# Main program loop
while True:
    print("What do you want to do?")
    print("1. Add a new task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. View tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task_name = input("Enter the task to add: ")
        add_task(task_name)
    elif choice == '2':
        task_index = int(input("Enter the index of the task to complete: ")) - 1
        complete_task(task_index)
    elif choice == '3':
        task_index = int(input("Enter the index of the task to remove: ")) - 1
        remove_task(task_index)
    elif choice == '4':
        print_tasks()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
