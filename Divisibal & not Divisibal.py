list=[5,8,7,6,15,25,35]
i=0
a=[]
y=[]
while i<len(list):
    b=list[i]
    if b%5==0:
        a.append(b)
    else:
        y.append(b)
    i=i+1
print("divisibal:",a,"not divisibal:", y)