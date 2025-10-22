FILE_NAME = "tasks.txt"
def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass  
    return tasks

def save_tasks(tasks):
    """Save all tasks to the file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("No tasks found. Add a new one!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task added: '{task}'")
    else:
        print("⚠️  Empty task not added.")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️  Removed: '{removed}'")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the number of the task to update: "))
        if 1 <= num <= len(tasks):
            new_text = input("Enter the updated task: ").strip()
            if new_text:
                old = tasks[num - 1]
                tasks[num - 1] = new_text
                save_tasks(tasks)
                print(f"🔄 Updated: '{old}' → '{new_text}'")
            else:
                print("⚠️  Empty update ignored.")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def main():
    print("👋 Welcome to Your Persistent To-Do List!")
    tasks = load_tasks()

    while True:
        print("\n========== MENU ==========")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Update task")
        print("5. Exit")
        print("==========================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            print("💾 Saving tasks... Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("⚠️  Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()

