num = int(input('Enter the Number'))
fact = 1
for i in range(2,num+1):
    fact*=i
print('Factorial of {} is {}'.format(num,fact))