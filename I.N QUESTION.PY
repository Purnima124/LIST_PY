# list1=["M","na","i","ke"]
# list2=["y","me","s","lly"]
# i=0
# y=[]
# j=0
# while i<len(list1):
#     k=list1[i]+list2[i]
#     y.append(k)
#     j+=1
#     i=i+1
# print(y)


# name=["snowball","chewy","Bubbles","Gurff"]
# animal=["cat","dog","Fish","Goat"]
# age=[1,2,2,6]
# i=0
# while i<len(name):
#     print(name[i],"the",animal[i],"is",age[i])
#     i=i+1
  



# list1=[10,20,[300,400,[5000,6000],500],30,40]
# list1[2][2].append(7000)
# print(list1)



# a=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# # print(a[2])
# b=[0]
# i=0
# while i<len(a):
#     if a[i]>b:
#         b=a[i]
#     i=i+1
# print(b)
#     else:
#         a[i]<b
#         b=a[i]
#     i=i+1
# print(b)




# def expanded_form(num):
#     i = 10**(len(str(num))-1)
#     ans = ''
#     while num:
#         if (num//i)*i != 0:
#             ans += str((num//i)*i) + ' + '
#         num = num % i
#         i //= 10
#     return (ans[0:len(ans)-3])

# # Test Cases
# print(expanded_form(42))
# print(expanded_form(12))
# print(expanded_form(70304))

# a=[[5,7,6],[8,12,21],[9,2,8]]
# i=0
