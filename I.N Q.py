# list=[3,4,5,[6,7],8]
# i=0
# while i<len(list):
#     j=0
#     k=list[i]
#     while j<len(list):
#         if list[i][j]>k:
#             k=[j][i]
#         j=j+1
#     i=i+1
#     print(k)

name=input("Enter the number ")
i=0
count=0
while i<len(name):
    k="a,e,i,o,u"
    if name[i] in k:
        count=count+1
        # print(count,"vovel")
    i=i+1
print(count,"vovel")