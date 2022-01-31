my_list=[1,2,"8",3,"AB",7,8]
i=0
n=[]
while i<len(my_list):
    if type(my_list[i])==int:
       n.append(my_list[i])
    else:
        pass
    i=i+1
print(n)
