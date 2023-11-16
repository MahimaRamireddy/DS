def binary_search(arr, low, high, x):
 
    
    if high >= low:
 
        mid = (high + low) // 2
 
        
        if arr[mid] == x:
            return mid
 
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
       
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        
        return -1

arr = []
n = int(input("Enter number of elements : "))
print("enter the elements : ")
for i in range(0, n):
    ele = int(input())
    arr.append(ele) 

print("Array: ")
print(arr)
arr.sort()

ser=int(input("enter the element you want to search for : "))

result = binary_search(arr, 0, len(arr)-1, ser)

if result != -1:
    print("Element is present in array.")
else:
    print("Element is not present in array!")