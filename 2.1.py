square = lambda x : x**2
num = int(input('Enter the range : '))
for i in range(1,num+1):
	print('Square of {} is {}'.format(i,square(i)))