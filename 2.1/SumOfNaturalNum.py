# Written by Shreyas Khadapkar
num = int(input('Enter the Number: '))
sum = 0
for i in range(1,num+1):
    sum += i 
print('The sum of {} natural numbers is {} '.format(num,sum))