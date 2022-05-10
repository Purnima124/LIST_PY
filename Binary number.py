binary_number=[1, 0, 0, 1, 1, 0, 1, 1]
# binary_number=[1,0,1]
i=0
sum=0
# len=len(binary_number)
# b=[]            
while i<len(binary_number):
    num1=binary_number[-i-1]
    sum=sum+num1*(2**i)
    i=i+1
print(sum)


























