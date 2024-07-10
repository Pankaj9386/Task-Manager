# #empty list
# list=[]
# print(list)

# #filled list

# list=['afha',34,45,'osadk']

# print(list)
# print(list[3]) # fourth element
# print(list[2:4]) # 3rd and 4th element

# #reverse list
# print("reverse list",list[::-1])

# #last two element
# print(list[-2:])

# #operations on the list

# #append
# list.append('lemon') # takes single argument
# print(list)

# #inserting the element at the required index
# list.insert(2,"286") 
# print(list)

# #pop function to remove last element
# x=list.pop()
# print(x)

# #print(list.remove(45)) shows none as it gets deleted
# print(list)
# list.remove(45)
# print(list)

# list2=[]
# list2=list
# print(list2) #copied entier list

# list3=['sfs','sdf',23]
# list3.append(list)
# print(list3)

# list2.append(list3[1])
# print(list2)

# for i in range(len(list)):
#     if i%2==0:
#         print(list[i],i)

# for i in list:
#     print(i)
    
# for list in list:
#     print(list)
# else:
#     print("list is over")

# y=34
# if 'sdf' in list:
#     print("the number is in list")

# if 244 in list3:
#     print("the number is in list")
# else:
#     print("not in the list")

# import os 
# f=open("3June\\project.py","w")
def fab(n):
    # if n==0 or n==1:
    #     return n
    # else:
    #     return (fab(n-1)+fab(n-2))
    a,b=0,1
    while a<=n:
        yield a
        a,b=b,a+b
    
limit=10    
for i in fab(limit):
    print(i)

