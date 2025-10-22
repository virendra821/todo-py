# todo-py
todo app in python
>Objective:
 ~ A simple console To-Do list that saves your tasks
 ~ automatically in a text file (tasks.txt).
>Features:
 ~ Uses a list to store tasks
 ~ Add / Remove / View / Update tasks
 ~ Automatically saves to tasks.txt
Insight=
 >Load tasks from file
      -If no file found, start with an empty list
 >Save tasks to file
 >View all tasks
 >Add a new task
 >Remove a task
 >Update a task
>>Main Menu
>            MENU
        1. View tasks
        2. Add task
        3. Remove task
        4. Update task
        5. Exit
>>behind the scenes
 ~The program uses a Python list (like a digital notepad) to hold all your tasks temporarily.
 ~The open() function is used to read and write to the file tasks.txt.
 ~Each line in that file is one task.
 ~Every time you change something (add, remove, update), the app writes the new list back into that file.
>>after opening todo.py it checks for saved tasks(If it finds it, it reads all your old tasks.
                                                   If not, it starts fresh with an empty list.)
                         then you see a simple menu (1. View tasks
                                                      2. Add task
                                                       3. Remove task
                                                        4. Update task
                                                         5. Exit)
                         When you add a task(You type something like “Finish homework.”  The program adds it to the list and saves it in tasks.txt.)
                         When you remove or update a task(You pick the task number, and it changes or deletes that task then it updates the tasks.txt file so it remembers.)
                         When you exit(The app automatically saves everything. Next time you open it, your tasks are still there.)
