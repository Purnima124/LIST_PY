num=[1,3,5,6,8,10,12]
i=0
a=[]
b=[]
while i<=(12):
    if i in (num):
        a.append(i)
    else:
        b.append(i)
    i=i+1
print(a,"persent no.")
print(b,"missing no.")
