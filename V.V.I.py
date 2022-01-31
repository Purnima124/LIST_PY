a=[1,2,3,4,"5","purnima",5,6,7]
i=0
n=[]
while i<len(a):
    if type(a[i])==str:
        n.append(a[i])
    # else:
    #     pass
    i=i+1
print(n)


