import math
import os
import random
import re
import sys
def superReducedString(s):
    if len(s)==1:
        return s
    ind=1
    while ind <len(s):
        print("s[{}]=P{}s={}".format(ind,s[ind],s))
        if s[ind]==s[ind-1]:
            if len(s)==2:
                return "empaty string"
            s=s[:ind-1]+s[ind+1:]
            ind=1
        else:
            ind+=1
    if len(s)==0:
        return "empty string"
    else:
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
