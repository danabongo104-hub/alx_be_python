task = input("Enter your task: ")
priority = input(" Whats is the priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

match priority:
    case "high":
        priority_level = "high"
    case "medium":
        priority_level = "medium"
    case "low":
        priority_level = "low"
    case _:
        priority_level = "unknown"
        
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_level} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_level} priority task. Consider completing it when you have free time.")