# Written by Shreyas Khadapkar
def isArmstrong(n):
    sum = 0
    for i in range (len(n)):
        sum+=int(n[i])**3
    if(sum== int(n)):
        return 1
    else:
        return 0

num = int(input('Enter the Range : '))
for i in range(num):
    if(isArmstrong(str(i))):
        print('{} is an Armstrong Number'.format(i))