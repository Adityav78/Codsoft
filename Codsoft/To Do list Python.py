tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!\n")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!\n")
    else:
        print("Task not found!\n1")

def display_tasks():
    if not tasks:
        print("No Task in the list!\n")
    else:
        print("Tasks:\n")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:

        print("\n*****  To-Do List *****\n")
        print("1. Add Task")
        print("2. Delete  Task")
        print("3. Display Task")
        print("4. Quit\n")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            task = input("Enter the Task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the Task to Delete: ")
            remove_task(task)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
         print("Invalid choice. Please enter a number from 1 to 4.\n")

if __name__ == "__main__":
    main()