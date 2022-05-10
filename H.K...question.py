num=[1,2,3,4,5,]
# i=0
i=0
a=num[0]
b=num[0]
while i<len(num):
    if num[i]>a or num[i]<b:
        a=num[i]+3
        b=num[i]-1
        i=i+a
        i=i+b
    i=i+1
print("menium:",b,"maximum",a)


    
# "maximum",a)
# or num[i]<b:


