# marks=[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# while i<len(marks):
#     a=0
#     s=0
#     while a<len(marks[i]):
#         s=s+(marks[i][a])
#         # sum=sum+1
#         a=a+1
#     sum=s+s
#     i=i+1
# print(sum)

list=[[5,5,5,5,5,5],[2,2,2,2,2,2],[3,3,3,3,3,3]]
i=0
sum=0
while i<len(list):
    j=0
    s=0
    while j<len(list[i]):
        s=s+(list[i][j])
        j=j+1
    sum=sum+s
    i=i+1
print(sum)

#     marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
# i=0
# sum=0
# while i<len(marks):
#     a=0
#     t=0
#     while a<len(marks[i]):
#         t=t+(marks[i][a])
#         a=a+1
#     sum=sum+t
#     i=i+1
# print("marks=",sum) 
