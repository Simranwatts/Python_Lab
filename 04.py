tasks = []

while True:
    print("\nTask Scheduler")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        condition = input("Enter condition (yes/no): ").lower()

        if condition == "yes":
            tasks.append((task, True))
        else:
            tasks.append((task, False))

        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for task, condition in tasks:
                if condition and True:
                    print("\nExecuting task:", task)
                    print("Condition satisfied. Task executed successfully.")
                elif not condition:
                    print("\nSkipping task:", task)
                    print("Condition not satisfied.")

    elif choice == "3":
        print("Exiting scheduler...")
        break

    else:
        print("Invalid choice.")
