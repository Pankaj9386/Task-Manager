dict1={0:1,1:2,2:2,'ramesh':4}

dict2={2:4,4:4,1:6,'ramesh':6}
dict3={}
id=0
newlist_same=[]
for i in dict1.keys():
    for j in dict2.keys():   
        if i==j:
            # id=dict1.keys
            dict3[i]=dict1[i] + dict2[j]
            newlist_same.append(i)
                    
for i in dict1.keys():
    if i not in newlist_same:
        dict3[i]=dict1[i]

for j in dict2.keys():
    if j not in newlist_same:
        dict3[j]=dict2[j]

   
print(dict3)

