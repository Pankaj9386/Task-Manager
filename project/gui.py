from tkinter import * 
import tkinter as tk
import project1
root = Tk()
root.title("Tak Manager")
root.geometry("600x400")
text_result=tk.Text(root,height=6, width=22,font=("Arial",24))
text_result.grid(columnspan=29)
scrollbar = Scrollbar(root)
scrollbar.grid(row=1, column=1, sticky="ns")
mylist = Listbox(root, command=project1.view())

    

# mylist.grid(row=1, column=0, sticky="nsew")
# scrollbar.config(command=mylist.yview)
# btn_1=tk.Button(root,text='New Task',command=(lambda x:project1.add_task(x)),width=15,font=("Arial",14))
# btn_1.grid(row=2,column=1)
# btn_2=tk.Button(root,text='Mark_as_completed',command=(lambda x:project1.add_task(x)),width=15,font=("Arial",14))
# btn_2.grid(row=2,column=1)
root.mainloop()


# import tkinter as tk
# import project1
 
# calulations=" "
 
# def add_to_caluculation(symbol):
#     global calulations
#     calulations += str(symbol)
#     text_result.delete(1.0,'end')#1.0 is specified for start
#     text_result.insert(1.0,calulations)
 
# def evaluate():
#     global calulations
#     try:
#         calulations=str(eval(calulations))
#         text_result.delete(1.0,'end')#1.0 is specified for start
#         text_result.insert(1.0,calulations)
#     except:
#         clear()
#         text_result.insert(1.0,"Error")
 
# def clear():
#     global calulations
#     calulations=" "
#     text_result.delete(1.0,'end')
 
 
# root=tk.Tk()
# root.title("calculator")
# root.geometry("400x300")
# text_result=tk.Text(root,height=2, width=22,font=("Arial",24))
# text_result.grid(columnspan=5)#the text_result will we spread over 5 columns
 
# btn_1=tk.Button(root,text='1',command=lambda:add_to_caluculation(1),width=5,font=("Arial",14))
# btn_1.grid(row=2,column=1)
# btn_2=tk.Button(root,text='2',command=lambda:add_to_caluculation(2),width=5,font=("Arial",14))
# btn_2.grid(row=2,column=2)
# btn_3=tk.Button(root,text='3',command=lambda:add_to_caluculation(3),width=5,font=("Arial",14))
# btn_3.grid(row=2,column=3)
# btn_4=tk.Button(root,text='4',command=lambda:add_to_caluculation(4),width=5,font=("Arial",14))
# btn_4.grid(row=3,column=1)
# btn_5=tk.Button(root,text='5',command=lambda:add_to_caluculation(5),width=5,font=("Arial",14))
# btn_5.grid(row=3,column=2)
# btn_6=tk.Button(root,text='6',command=lambda:add_to_caluculation(6),width=5,font=("Arial",14))
# btn_6.grid(row=3,column=3)
# btn_7=tk.Button(root,text='7',command=lambda:add_to_caluculation(7),width=5,font=("Arial",14))
# btn_7.grid(row=4,column=1)
# btn_8=tk.Button(root,text='8',command=lambda:add_to_caluculation(8),width=5,font=("Arial",14))
# btn_8.grid(row=4,column=2)
# btn_9=tk.Button(root,text='9',command=lambda:add_to_caluculation(9),width=5,font=("Arial",14))
# btn_9.grid(row=4,column=3)
# btn_0=tk.Button(root,text='0',command=lambda:add_to_caluculation(0),width=5,font=("Arial",14))
# btn_0.grid(row=5,column=2)
# btn_plus=tk.Button(root,text='+',command=lambda:add_to_caluculation('+'),width=5,font=("Arial",14))
# btn_plus.grid(row=2,column=4)
# btn_minus=tk.Button(root,text='-',command=lambda:add_to_caluculation('-'),width=5,font=("Arial",14))
# btn_minus.grid(row=3,column=4)
# btn_div=tk.Button(root,text='/',command=lambda:add_to_caluculation('/'),width=5,font=("Arial",14))
# btn_div.grid(row=4,column=4)
# btn_mult=tk.Button(root,text='*',command=lambda:add_to_caluculation('*'),width=5,font=("Arial",14))
# btn_mult.grid(row=5,column=4)
# btn_open=tk.Button(root,text='(',command=lambda:add_to_caluculation('('),width=5,font=("Arial",14))
# btn_open.grid(row=5,column=1)
# btn_close=tk.Button(root,text=')',command=lambda:add_to_caluculation(')'),width=5,font=("Arial",14))
# btn_close.grid(row=5,column=3)
# btn_clear=tk.Button(root,text='C',command=clear,width=14,font=("Arial",14))
# btn_clear.grid(row=6,column=1,columnspan=2)
# btn_equals=tk.Button(root,text='=',command=lambda:evaluate(),width=14,font=("Arial",14),bg="red")
# btn_equals.grid(row=6,column=3,columnspan=2)
# root.mainloop()
 