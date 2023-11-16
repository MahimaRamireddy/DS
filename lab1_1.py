def InsertionSort(a):
  
    
    for i in range(1, len(a)):
  
        temp = a[i]
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp
       
arr = []
n=int(input("enter the number of elements : "))
print("enter elements : ")
for i in range(0, n):
    ele = int(input())
    arr.append(ele) 


print("Array before sorting:")
print(arr)

InsertionSort(arr)

print("Array after sorting:")
print(arr)