def primepartition(num):
    primelist=[]
    for i in range(2,num + 1):
        for p in range(2,i):
            if (i % p) == 0:
                break
        else:
            primelist.append(i)
 
    for x in primelist:
        y= num-x
        if y in primelist:
            print(True)
            return True
        else:
            print(False)
            return False
 
m = 33
primepartition(m)
n = 75
primepartition(n)
