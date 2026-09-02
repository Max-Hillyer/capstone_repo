import os

tasks = {}

while True:
    os.system("clear")
    print("tasks: ")

    tasks = dict(sorted(tasks.items(), key=lambda item: item[1]))

    for t, c in tasks.items():
        if c < 3:
            print(f"[{'x' if c == 2 else ' '}] {t}")

    newTask = input("Enter a task: ")

    if newTask in tasks:
        tasks[newTask] += 1
    else:
        tasks[newTask] = 1
