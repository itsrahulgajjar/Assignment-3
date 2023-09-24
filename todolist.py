# todolist.py

tasks = []

<<<<<<< HEAD
def add_task(task):
    tasks.append(task)
=======
def add_task(task, priority):
    tasks.append({"task": task, "priority": priority})
>>>>>>> feature

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def complete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
    else:
        print("Invalid task number")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to complete: "))
            complete_task(index)
        elif choice == "4":
            break
