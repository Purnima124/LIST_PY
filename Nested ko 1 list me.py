a=[[1,2,3],[10,18],[7,2]]
n=[]
i=0
while i <len(a):
    # if i<3:
    j=0
    while j<len(a[i]):
        n.append(a[i][j])
        j=j+1
    i=i+1
print(n)