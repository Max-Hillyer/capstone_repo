import os
import sys

tasks = {}

while True:
    if (sys.platform) == "darwin":
        os.system("clear")
    else:
        os.system("cls")

    print("tasks: ")

    tasks = dict(sorted(tasks.items(), key=lambda item: item[1]))

    for t, c in tasks.items():
        if not (c % 3 == 0):
            print(f"[{'x' if c == 2 else ' '}] {t}")

    newTask = input("Enter a task: ")

    if newTask in tasks:
        tasks[newTask] += 1
    else:
        tasks[newTask] = 1
