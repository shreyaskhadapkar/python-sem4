def inverse(n):
    rev = 0
    while(n>0):
        r = n%10
        rev = (rev*10)+r
        n = n//10
    print("The reverse of the number is : " , rev)
n = int(input("Please enter a number : "))
inverse(n)
