def lcm(a,b):
    if(a>b):
        greater = a
    else:
        greater = b
    while(1):
        if (greater%a==0) and (greater%b == 0):
            lcm =  greater
            break
        greater += 1

    return lcm
    
a,b = map(int,input('Enter the two numbers: ').split())
print(lcm(a,b))