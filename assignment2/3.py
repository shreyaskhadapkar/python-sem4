def sumprime(l):
    sum = 0
    for i in range(0,len(l)):
        num = l[i]
        prime = True
        for j in range(2, int(num**0.5)+1):
            if num%j == 0:
                prime = False
                break
        if prime:
            sum = sum + num
    print("The sum of all prime numbers in the list are : " ,sum)
 
l = [2,3,7,4,17]
sumprime(l)  
