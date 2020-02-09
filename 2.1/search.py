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