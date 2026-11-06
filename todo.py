# To-Do List Application
# Python Developer Internship - Task 2

# Function to load tasks from the file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        tasks = []

    return tasks


# Function to save tasks into the file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # Add Task
        if choice == "1":
            task = input("Enter a new task: ").strip()

            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        # View Tasks
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        # Remove Task
        elif choice == "3":
            if not tasks:
                print("No tasks available to remove.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        save_tasks(tasks)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        # Exit
        elif choice == "4":
            print("Thank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


# Run the application
if __name__ == "__main__":
    main()