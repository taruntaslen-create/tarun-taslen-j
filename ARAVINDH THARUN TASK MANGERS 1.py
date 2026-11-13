
tasks = []
completed = []

while True:
    print("\nPERSONAL TASK MANAGER ")
    print("1. Add Task")
    print("2. View Pending Tasks")
    print("3. Mark Task Completed")
    print("4. View Completed Tasks")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        priority = input("Enter priority (High/Medium/Low): ")
        deadline = input("Enter deadline: ")

        tasks.append([task, priority, deadline])
        print("Task added successfully!")

    elif choice == "2":
        print("\nPending Tasks:")
        for i, task in enumerate(tasks):
            print(i + 1, task)

    elif choice == "3":
        for i, task in enumerate(tasks):
            print(i + 1, task)

        num = int(input("Enter task number: "))

        if 1 <= num <= len(tasks):
            completed.append(tasks.pop(num - 1))
            print("Task completed!")

        else:
            print("Invalid task number!")

    elif choice == "4":
        print("\nCompleted Tasks:")
        for task in completed:
            print(task)

    elif choice == "5":
        for i, task in enumerate(tasks):
            print(i + 1, task)

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")

        else:
            print("Invalid task number!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
