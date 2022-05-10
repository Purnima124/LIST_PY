# a=["rahul",12,9.0,"kaavay","shivam",1]
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
# print(a[-5])
# print(a[-6])
num=[23,14,56,12,19,9,15,25,31,42,93]
i=0
a=[]
c=0
a=0
sum1=0
sum2=0
sum=0
sum3=0
c1=0
c2=0
c3=0
while i<len(num):
    k=sum[i]
    if k%2==0:
        a.append(k)
        sum1=sum1+k
        c=sum1//len(a)
        c1=c1+1
    else:
        b.append(k)
        sum2=sum2+k
        c=sum2//len(b)
    sum3=sum1+sum2
    sum=sum3//len(a+b)
    c2=c2+1
    c3=c2+c1
    i=i+1
print("even",a,"count",c,"odd",b,"count",c2)
print("Total count",c3)
print("even sum",sum1,"odd sum",sum2)
print("even evrege",c,"odd evrage",d)
