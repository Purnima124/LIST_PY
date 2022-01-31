a=[2,3,[4,5]]
n=[]
i=0
while i <len(a):
    if i<2:
        n.append(a[i])
    else:
        j=0
        while j<len(a[i]):
            n.append(a[i][j])
            j=j+1
    i=i+1
print(n)