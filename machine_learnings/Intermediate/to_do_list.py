#Create a simple to-do list using a dictionary
List=[]

print("Input values:\n"
"1. Add Task\n"
'2. Edit Task\n'
'3. Delete Task\n'
"4. Exit")
number=int(input("Enter number (1 to 4): "))
def add_task():
    a=input("Enter task")
    List.append(a)    
    print(List)
    print("Output value:\n"
"Task added successfully.")
def edit_task():
    input("Enter task index to edit:")
def delete_task():
    b=input("Enter task index to delete: ")
    List.remove(b)
    print("Output value:\n"
"Task deleted successfully.")
def exit():
    print("exit")

if number==1:
    add_task()
elif number==2:
    edit_task()
elif number==3:
    delete_task()
elif number==4:
    exit()
else:
    print("please ender correct number")