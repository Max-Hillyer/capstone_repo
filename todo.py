import os
import sys

tasks = {}

while True:
    if (sys.platform) == "darwin":
        os.system("clear")
    else:
        os.system("cls")

    print("Tasks: \n")

    tasks = dict(sorted(tasks.items(), key=lambda item: item[1]))

    for t, c in tasks.items():
        print(f"[{'x' if c == 2 else ' '}] {t}")

    newTask = input("\nEnter a task: ")

    if "__exit__" == str(newTask).lower(): exit(0)

    if newTask in tasks:
        tasks[newTask] += 1
    else:
        tasks[newTask] = 1

    for key in list(tasks):
        if tasks[key] > 2:
            del tasks[key]
