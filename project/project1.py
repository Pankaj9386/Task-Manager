import os
def add_task():    
    title=input("enter title of task: ")
    with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt",'x')as f:
        z=input("enter the task: ")
        f.write(z)
        
    return "task added"


def delete_task():
    contents=os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    print("=================\nbelow are the tasks saved\n")
    for item in contents:
        if ".txt" in item:
            print(item[:-4])
    print("=================")
    os.listdir("project")    
    title=input("enter title of task to delete ")
    os.remove(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt")
    
    return "task deleted"

def mark_as_completed():
    flag=0
    u=input("enter y to view file to mark as completed ")
    contents=os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    print("=================\nbelow are the tasks saved\n")
    for item in contents:
        if ".txt" in item:
            print(item[:-4])
    print("=================")
    while u=='y':
        try:
            title=input("enter title of task: ")
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt",'r')as f:
                z=f.read()
            os.remove(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt")    
            
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed\\{title}.txt",'x')as f:
                f.write(z)
            flag=1 
        except FileNotFoundError:
            print("Invalid title")
            u=input("enter y to continue: ")
        
    if flag==1:
        return "mark as Completed"
    else:
        return "not marked"
        
def view():
    contents=os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    print("=================\n tasks are given beloew\n")
    for item in contents:
        if ".txt" in item:
            print(item[:-4])
    print("=================")
        
    u=input("enter y to view file: ")
    while u=='y':        
        try:   
            title=input("enter title of task: ")
            
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt",'r')as f:
                print("============")
                print("here is your task")
                print(title)            
                print("task details: ",f.read())
                u=input("enter y to continue")
        except:
            print("invalid credentials")
            u=input("enter y to continue: ")
    
def open_marked_as_completed():    
    contents=os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed")
    print("=================\nbelow are the files marked as completed\n")
    for item in contents:
        if ".txt" in item:
            print(item[:-4])
    print("=================")
    u=input("enter y to view file: ")
    while u=='y': 
        try:   
            title=input("enter title of task: ")
            os.listdir("marked_As_completed")
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed\\{title}.txt",'r') as f:
                print("============")
                print("here is your task")
                print(title)            
                print("task details: ",f.read())
        except:
            print("invalid credentials")
            u=input("enter y to continue: ")
    
if __name__=="__main__":
           
    u=input("enter y to view main operations: ")
    while u=='y':
        z=int(input("1:new task\t2:mark as completed\t3:delete\t4:view\t5:open_marked_as_completed: "))
        match z:
            case 1:
                add_task()
            case 2:
                mark_as_completed()
            case 3:
                delete_task()
            case 4:
                view()
            case 5:
                open_marked_as_completed()   
            
                
        u=input("enter y to continue in operations: ")   

        

