num=[50,40,23,70,56,12,5,10,7]
i=0
a=num[i]
while i<len(num):
    if num[i]>a:
        a=num[i]
    i=i+1
num.remove(a)
i=0
l=num[i]
while i <len(num):
    if num[i]>l:
        l=num[i]
    i=i+1
print(l)
# 
# a=[-1,-2,-3,-4,-5]
# i=0
# n=a[i]
# while i<len(a):
    # if a[i]>n:
        # n=a[i]
    # i=i+1
# print(i)