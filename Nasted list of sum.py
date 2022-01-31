a=[[2,5,6],[7,8,9],[12,16,11]]
i=0
sum=0
while i<len(a):
    j=0
    d=0
    while j<len(a[i]):
        d=d+a[i][j]
        j=j+1
    sum=sum+d
    i=i+1
print(sum)

# a=[1,2,3,[6,2,5],[7,8],[3,9,0],5,6,[7,8]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     d=0
#     while j<len(a[i]):
#         d=d+a[i][j]
#         j=j+1
#     sum=sum+d
#     i=i+1
# print(sum)