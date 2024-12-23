task = input("please enter a task description.")

priority = input("please enter a task priority (high, medium, low)")

time_bound = input("is this task time bounf? (yes or no)")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that requires attention before deadline!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task that requires attention before deadline!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires attention before deadline!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")