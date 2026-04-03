addtasks=[]
import csv
i=0

try:
    with open("input.txt", "r") as file:
        for line in file:
            addtasks.append(line.strip())
except FileNotFoundError:
    pass

def main_menu():
    
    while (True):
        print("1. Add a task")
        print("2. view tasks")
        print("3. delete tasks")
        print("4. quit")
        go_to=input("Where would you like to go: ")
                    
        try:
            x=int(go_to)
            if (x == 1 ):
                add_task()

            elif (x == 2 ):
                view_task()

            elif (x == 3 ):
                del_tasks()

            elif (x == 4 ):
                
                quit()

        except ValueError:
            print("please respond with a proper input")


def add_task():
    while(True):
        currentTask = input("what task would you like to add: ")
        addtasks.append(currentTask)
        txt_data = currentTask + "\n"

        with open(file_path, "a") as file:
            file.write(txt_data)
            print(f"txt file '{file_path}' has been saved")


        response = input("would you like to add another task y/n ")
        if (response.lower() == "y"):
            len(addtasks)

        elif(response.lower() == "n"):
            break

        else:
            print("please use a provided a valid input")

    return

def view_task():

    if len(addtasks) == 0:
        print("No tasks available")

    i = 0
    for x in addtasks:
        i+=1
        print(i," ", x)

    while(True):
        uin = input("press y when you would like to go back to the main menu ")
        if (uin.lower() == "y"):
            break

        else:
            print("please use a provided a valid input")

    return

def del_tasks():
    while(True):
        del_task = input("have you completed any tasks y/n ")
        if(del_task.lower() == "y"):
            task_loc = input("please input the task number you wish to remove? ")

            try:
                z=int(task_loc)

                if(z > 0 and z <= len(addtasks) ):
                    addtasks.pop(z-1)
                    i = 0
                    for x in addtasks:
                        i+=1
                        print(i," ", x)

                    with open("input.txt", "w") as file:
                        print("tasks have been updated")
                        for task in addtasks:
                            file.write(task + "\n")
                else:
                    print("please input an integer: What task number do you wish to remove? ")
                    task_loc = input("please input the task number you wish to remove? ")

            except ValueError:
                print("not a number")

        elif(del_task.lower() == "n"):
            break
    return
            
file_path = "input.txt"    
main_menu()