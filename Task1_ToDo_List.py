# CODSOFT - Task 1
# To-Do List Application

tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- YOUR TASKS ---")

        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} - {status}")


def add_task():
    task_name = input("\nEnter your task: ")

    if task_name.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append({
            "name": task_name,
            "completed": False
        })

        print("Task added successfully!")


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task '{removed['name']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n========================")
    print("       TO-DO LIST")
    print("========================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
