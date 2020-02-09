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