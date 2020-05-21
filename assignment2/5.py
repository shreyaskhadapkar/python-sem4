def rotatelist(l,k):
    for i in range(0, k):    
        first = l[0]    
            
        for j in range(0, len(l)-1):    
            l[j] = l[j+1]   
                
        l[len(l)-1] = first  
        
    print("Array after left rotation: ", l)  
    
l = [1, 2, 3, 4, 5]
k = int(input("Enter number of rotations: "))
if k < 1:
    print("Cannot rotate the list")
else:
    rotatelist(l,k)