import os
import streamlit as st

def add_task():
    title = st.text_input("Enter title of task:")
    task = st.text_area("Enter the task:")
    if st.button("Add Task"):
        with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{title}.txt", 'w') as f:
            f.write(task)
        st.success("Task added successfully!")

       
def delete_task():
    contents = os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    task_list = [item[:-4] for item in contents if ".txt" in item]
    st.write("Tasks:")
    # selected_task = st.selectbox("Select task to delete:", task_list)
    selected_task = st.radio("Select an option:", task_list)
    st.write(selected_task)
    with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{selected_task}.txt","r")as f:
                z=f.read()
                st.write(z)
    if st.button("Delete Task"):
        
            
            # st.write(selected_task)
            # with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{selected_task}.txt","r")as f:
            #     z=f.read()
            #     st.write(z)               
            os.remove(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{selected_task}.txt")
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\deleted\\{selected_task}.txt","x")as f:
                f.write(z)
            st.success("Task deleted successfully!")
        

def mark_as_completed():
    contents = os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    task_list = [item[:-4] for item in contents if ".txt" in item]
    selected_task = st.selectbox("Select task to mark as completed:", task_list)
    if st.button("Mark as Completed"):
        try:
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{selected_task}.txt", 'r') as f:
                task_content = f.read()
            os.remove(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{selected_task}.txt")
            with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed\\{selected_task}.txt", 'w') as f:
                f.write(task_content)
            st.success("Task marked as completed!")
        except FileNotFoundError:
            st.error("Task not found!")

def view_tasks():
    contents = os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project")
    task_list = [item[:-4] for item in contents if ".txt" in item]
    st.write("Tasks:")
    radio = st.radio("Select an option:", task_list)
    st.write(radio)
    with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{radio}.txt","r")as f:
        z=f.read()
        st.write(z)
    # for task in task_list:
    #     st.write(task)
        # contents = os.listdir(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\{task}")
        

def view_completed_tasks():
    contents = os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed")
    task_list = [item[:-4] for item in contents if ".txt" in item]
    st.write("Completed Tasks:")
    radio = st.radio("Select an option:", task_list)
    st.write(radio)
    with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\marked_As_completed\\{radio}.txt","r")as f:
        z=f.read()
        st.write(z)

def view_Deleted_tasks():
    contents = os.listdir("C:\\Users\\dP-PL\\Desktop\\python\\project\\deleted")
    task_list = [item[:-4] for item in contents if ".txt" in item]
    if len(task_list)==0:
        st.write("No file deleted")
    else:
        
        st.write("Deleted Tasks:")
        # for task in task_list:
        #     st.write(task)
        radio = st.radio("Select an option:", task_list)
        st.write(radio)
        with open(f"C:\\Users\\dP-PL\\Desktop\\python\\project\\deleted\\{radio}.txt","r")as f:
            z=f.read()
            st.write(z)


def main():
    st.title("Task Manager")
    button_options=["+","<completed>","X"]
    
    # if st.button("ADD NEW"):
    #     add_task()
    # if st.button("Delete Task"):
    #     delete_task()
    # if st.button("mark as Completed"):
    #     mark_as_completed()
    # if st.button("View Tasks"):
    #     view_tasks()
    # if st.button("View Completed Tasks"):
    #     view_completed_tasks()
    # col1, col2, col3, col4, col5 = st.columns(5)
    
    # with col1:
    #     if st.button("ADD NEW",key="add"):
    #         add_task()
            
    # with col2:
    #     if st.button("Delete Task",key="delete"):
    #         delete_task()
            
    # with col3:
    #     if st.button("Mark as Completed",key="mark"):
    #         mark_as_completed()
            
    # with col4:
    #     if st.button("View Tasks",key="view"):
    #         view_tasks()
            
    # with col5:
    #     if st.button("View Completed Tasks",key="completed"):
    #         view_completed_tasks()
    
    options = ["None","Add Task", "Delete Task", "Mark as Completed", "View Tasks", "View Completed Tasks","View Deleted Tasks"]
    choice = st.sidebar.selectbox("Select an option:", options)
    
    if choice == "None":
        pass
    elif choice=="Add Task":
        add_task()
    elif choice == "Delete Task":
        delete_task()
    elif choice == "Mark as Completed":
        mark_as_completed()
    elif choice == "View Tasks":
        view_tasks()
    elif choice == "View Completed Tasks":
        view_completed_tasks()
    elif choice == "View Deleted Tasks":
        view_Deleted_tasks()

if __name__ == "__main__":
    main()
