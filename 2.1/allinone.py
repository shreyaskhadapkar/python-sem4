# Written by Shreyas Khadapkar
print('Armstrong Number')
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

print()
print('Armstrong in a Range')
print()

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


print()
print('To check if number is positive or negative')
print()

# Written by Shreyas Khadapkar
num = int(input('Enter the Number: '))
if num>0:
    print('Number is Positive')
elif num<0:
    print('Number is Negative')
elif num == 0:
    print('Number is Zero')
else:
    print('Entered Number is Not a valid Number')



print()
print('Prime NUmber')
print()
#written by Shreyas KhadapkaR
import math
num = int(input('Enter the Number : '))
if num > 1:
   for i in range(2,int(math.sqrt(num))+1):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


num = int(input('Enter the Number'))
fact = 1
for i in range(2,num+1):
    fact*=i
print('Factorial of {} is {}'.format(num,fact))



print()
print('Fibonacci Number')
print()
# Written by Shreyas Khadapkar
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

num = int(input('Enter the Number: '))
print('Fibonacci Series is as follows : ')
for i in range(num):
    print(fibo(i))


print()
print('Largest Among 3 numbers')
print()
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


print()
print('Leap Year')
print()
# Written by Shreyas Khadapkar
year = int(input('Enter the Year: '))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{} is a leap year".format(year))
       else:
           print("{} is not a leap year".format(year))
   else:
       print("{} is a leap year".format(year))
else:
   print("{} is not a leap year".format(year))



print()
print('Multiplication Table')
print()
# Written by Shreyas Khadapkar
num = int(input('Enter the Number : '))
for i in range(1,11):
    print('{} * {} = {} '.format(num,i,num*i))


print()
print('To check if number is Odd or Even ')
print()
# Written by Shreyas Khadapkar
num = int(input('Enter the Number: '))
if (num%2):
    print('Entered Number is Odd')
else:
    print('Entered Number is Even')

print()
print('Prime NUmber in range')
print()
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


print()
print('To find the roots of the given Equation')
print()
import math
a = int(input('Enter the value of a'))
b = int(input('Enter the value of b'))
c = int(input('Enter the value of c'))

d = (b*b) - (4*a*c)
if d<0:
    print('There are no Real Solutions')
else:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print('Real roots are {} and {} '.format(r1,r2))



print()
print('Search Algorithms')
print()
def search(list,n): 
  
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False

list = [1, 2, 'shreyas', 4,'python', 6] 

n = input('Enter the element to be searched: ')
if n.isnumeric():
    n = int(n)
  
if search(list, n): 
    print("Found") 
else: 
    print("Not Found")


print()
print('Sorting Algorithms')
print()
print('Using Built in .sort() function')
print()
numbers = [1, 3, 4, 2] 
numbers.sort()
print(numbers) 

decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 
decimalnumber.sort() 
print(decimalnumber) 

words = ["Python", "For", "Shreyas"] 
words.sort() 
print(words)
print()
print('Using Bubble Sort')
print()
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [68, 34, 22, 12, 33, 11, 99]
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])



print()
print('Sum of Natural Numbers')
print()
# Written by Shreyas Khadapkar
num = int(input('Enter the Number: '))
sum = 0
for i in range(1,num+1):
    sum += i 
print('The sum of {} natural numbers is {} '.format(num,sum))



print()
print('To count Vowels and Consonants in a string')
print()
# Written by Shreyas Khadapkar      
string = input('Enter the string : ')
# print(len(string))
string = string.lower()
vowels,cons = 0,0
# print(vowels,cons)
# print(string)
for i in range(len(string)):
    if(string[i].isalpha()):
        # print('hi')
        if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
            vowels+=1
        else:
            cons+=1
    # else:
    #     print('else')
print('The input string contains {} vowels and {} consonants'.format(vowels,cons))