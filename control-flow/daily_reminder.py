task = input("Enter your task: ")

time_bound = input("Is it time-bound? (yes/no): ")
git add
priority = input("Priority (high/medium/low): ")

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