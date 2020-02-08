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