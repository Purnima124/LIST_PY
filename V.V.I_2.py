# name=input("enter name :")
# i=0
# while i<len(name[i]):
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")
#     i=i+1


# num=int(input("enter number "))
# if num=="second number 2":
#     print("yes")
# else:
#     print("no")


a=["True","false","True","Tare","false"]
i=0
list1=[]
count=0
count1=0
while i<len(a):
    if a[i]=="True":
        b=a[i]
        count+=1
    else:
        pass
    i=i+1
if count>count1:
    list1.append(b)
    print(list1)
else:
    list1.append(count)
    print(list1)


