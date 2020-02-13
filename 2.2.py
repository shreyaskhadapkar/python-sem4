r = list(map(int,input('Enter the List of numbers : ').split()))
#print(r)
num = int(input('Enter the number for divisibility test : '))
div = lambda x : x%num == 0
print(list(filter(div,r)))