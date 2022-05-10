elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
b=[]
while i<len(elements):
    k=elements[i]
    if k%2==0:
        a.append(k)
    else:
        b.append(k)
    i=i+1
print("even",a)
print("odd",b)


