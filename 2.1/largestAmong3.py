# Written by Shreyas Khadapkar
n1 = int(input('Enter the first Numbers : '))
n2 = int(input('Enter the Second Numbers : '))
n3 = int(input('Enter the third Numbers : '))
# print(n1,n2,n3)
if(n1>n2 and n1>n3):
    print('{} is Largest'.format(n1))
elif(n2>n1 and n2>n3):
    print('{} is Largest'.format(n2))
else:
    print('{} is Largest'.format(n3))