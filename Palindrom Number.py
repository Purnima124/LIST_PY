a=["n","i","t","i","n"]
i=1
y=[]
while i<=len(a):
    y.append(a[-i])
    i=i+1
if y==a:
    print(y,"palindrome")
else:
    print(y,"not")


    