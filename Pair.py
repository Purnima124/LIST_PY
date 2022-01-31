list1=[1,2,3,1,1,2,3,3,3,1]
i=0
a=[]
b=[]
while i<len(list1):
    count1=0
    m=list1[i]
    j=0
    while j<len(list1):
        n=list1[j]
        if m==n:
            a.append(n)
            count1=count1+1
        j=j+1
    k=0
    while k<len(list1):
        if m not in a:
            b.append(m)
            count1=count1+1
            # print(m,"=",count1,"pair")
        k=k+1
    i=i+1
print(m,"=",count1,"pair")