n=[]
i=1
while i<=len(a):
    b=a[-i]
    n.append(b)
    i=i+1
print(n)
input=int(input("Enter the name"))
a=b[-1::-1]
if(a==a[::-1]):
    print("p")
else:
    print("not p")

