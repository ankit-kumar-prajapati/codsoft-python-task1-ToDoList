lst=[]
def create_task():
    dict={'number':-1,'task':'','status':'Not completed'}
    num=input('Enter the task number : ')
    dict['number']=num
    task=input('Enter the task : ')
    dict['task']=task
    lst.append(dict)
    print('Task added successfully!')
def delete_task():
    task_found=False
    num=input("Enter the task number : ")
    for i in range(len(lst)):
        if (lst[i]['number']==num):
            lst.pop(i)
            task_found=True
            print('Task deleted successfully!')
    if not task_found:
        print('Task number not found')
def update_task():
    task_found=False
    num=input("Enter the task number : ")
    for i in range(len(lst)):
        if (lst[i]['number']==num):
            lst[i]['status']='Completed'
            task_found=True
            print('Task updated successfully!')
    if not task_found:
        print('Task number not found')
def view_to_do_list():
    for i in lst:
        print(f"{i['number']}. {i['task']} ({i['status']})")
print("Enter your choice : \n1. Create task \n2. Update task \n3. Delete task \n4. View To-Do List \n")
try : 
    choice=int(input("Enter your choice (enter the option number) : "))
    print()
except ValueError:
    choice=-1
while(choice!=0):
    if choice!=1 and choice!=2 and choice!=3 and choice!=4:
        print("Wrong choice entered. Try again!")
    else :
        if choice==1:
            create_task()
            print()
        elif choice==2:
            update_task()
            print()
        elif choice==3 :
            delete_task()
            print()
        else:
            view_to_do_list()
            print()
    print("Enter your choice : \n0. Exit \n1. Create task \n2. Update task \n3. Delete task \n4. View To-Do List \n")
    try : 
        choice=int(input("Enter your choice (enter the option number) : "))
        print()
    except ValueError:
        choice=-1
        