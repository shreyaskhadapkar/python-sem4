#written by Shreyas KhadapkaR
import math
def checkPrime(num):
    count = 0
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0
num = int(input('Enter the Range : '))
for i in range(num+1):
    if(checkPrime(i)):
        print(i," is Prime Number")

