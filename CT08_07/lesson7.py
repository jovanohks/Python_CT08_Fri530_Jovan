import os
filepath=os.getcwd()
tasks_path=os.path.join(filepath,"tasks.txt")
if os.path.exists(tasks_path):
    print("tasks exists")
    overwrite= input("overwrite existing file(Y/N)").lower()
    if overwrite=="y":
        with open("tasks.txt","w") as file:
            file.write("My Tasks List\n")
    else:
        print("file will not be overwritten.")
else:
    print("tasks does not exists")
    with open("tasks.txt","w") as file:
            file.write("My Tasks List\n")
    print("New tasks file created.")
with open("tasks.txt","a") as file:
    x=input("add new task")
    file.write("\n"+x)
with open("tasks.txt","r") as file:
    lines=file.readlines()
    print(lines)
    for i in range(len(lines)):
        if i==0:
            print(lines[i].strip())
        else:
            print(f"{i}. {lines[i].strip()}")
task_done =input("enter the task number to mark as done.")
lines[task_done] =="Done"