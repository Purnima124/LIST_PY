num1=int(input("enter the number "))
num=[1,2,3,4,5,6,7]
i=0
k=[]
while i<len(num)-num1:
    k.append(num[i])
    i=i+1
j=1
while j<=num1:
    k.append(num[-j])
    j=j+1
print(k)
