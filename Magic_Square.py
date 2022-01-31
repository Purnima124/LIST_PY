# magic_square=[
#     [8,3,4],
#     [1,5,9],
#     [6,7,2]

# ]
# i=0
# while i<len(magic_square):
#     j=0
#     sum=0
#     while j<len(magic_square):
#         sum=sum+magic_square[i][j]
#         j=j+1
#     i=i+1
# print(sum)
# a=0
# while a<len(magic_square):
#     k=0
#     sum1=0
#     while k<len(magic_square):
#         sum1=sum1+magic_square[a][k]
#         k=k+1
#     a=a+1
# print(sum1,)


magic_square=[
    [8,3,4],
    [0,0,0],
    [6,7,2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+magic_square[j][i]
        j=j+1
    i=i+1
print(sum)
a=0
while a<len(magic_square):
    k=0
    sum1=0
    while k<len(magic_square):
        sum1=sum1+magic_square[k][a]
        k=k+1
    a=a+1
print(sum1)
j=0
while j<len(magic_square):
    n=0
    sum2=0
    while n<len(magic_square):
        sum2=sum2+magic_square[n][j]
        n=n+1
    j=j+1
print(sum2)



# if sum==sum1 and sum==sum2:
#     print("it is magic_square")
#     if sum!=sum1 or sum!=sum2:
#         print("not")
#     # print(sum1)
# else:
#     print("try again")















