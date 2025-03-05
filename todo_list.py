import json

# Functions from previous steps
def add_task(tasks, task_description):
    task = {"task": task_description, "status": "Pending"}
    tasks.append(task)
    print(f'Task "{task_description}" added successfully!')

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']} - [{task['status']}]")

def complete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Completed"
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" deleted successfully!')
    else:
        print("Invalid task number.")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main Menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task_desc = input("Enter task description: ")
            add_task(tasks, task_desc)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                complete_task(tasks, task_num)
            except ValueError:
                print("Invalid input, please enter a number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                delete_task(tasks, task_num)
            except ValueError:
                print("Invalid input, please enter a number.")
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
