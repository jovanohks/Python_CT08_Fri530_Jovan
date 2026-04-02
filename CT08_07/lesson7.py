import os
filepath=os.getcwd()
tasks_path=os.path.join(filepath,"tasks.txt")
if os.path.exists(tasks_path):
    print("tasks exists")
    overwrite= input("overwrite existing file(Y/N) ").lower()
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
def add_task():
    with open("tasks.txt","a") as file:
        x=input("add new task: ")
        file.write(x+"\n")
def view_all_tasks():
    with open("tasks.txt","r") as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if i==0:
                print(lines[i].strip())
            else:
                print(f"{i}. {lines[i].strip()}")
def delete():
    view_all_tasks()
    task_number=int(input("enter the task number to delete: "))
    with open("tasks.txt","r") as file:
        lines=file.readlines()
    lines.pop(task_number)
    with open("tasks.txt","w") as file:
        file.writelines(lines)
def done():
    view_all_tasks()
    with open("tasks.txt","r") as file:
        lines=file.readlines()
    task_number=int(input("which number to mark done?"))
    if task_number <1 and task_number>= len(lines):
        print("index is invalid please give a valid index")
        return
    lines[task_number] = lines[task_number].strip() +" (done)"
    with open("tasks.txt","w") as file:
        file.writelines(lines)
    print("task marked as done.")
def menu():
    print("1.view all tasks")
    print("2.add new task")
    print("3.delete tasks")
    print("4.mark task as done")
    print("5.exit")
while True:
    menu()
    x=input("which choice do you want?")
    if x=="1":
        view_all_tasks()
    elif x=="2":
        add_task()
    elif x=="3":
        delete()
    elif x=="4":
        done()
    elif x=="5":
        break