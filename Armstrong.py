# Written by Shreyas Khadapkar
num = input('Enter the Number: ')
sum = 0
# num1 = num
# print(num)
# num[0]

for i in range (len(num)):
    sum+=int(num[i])**3
    # print(sum,i)

if(sum == int(num)):
    print('Given Number is Armstrong Number')
else:
    print('Given Number is NOT a Armstrong Number')