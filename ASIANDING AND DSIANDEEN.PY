a=[4,8,6,9]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a [i]>a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
print(a)


