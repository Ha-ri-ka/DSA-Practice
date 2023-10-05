def recurInsertionSort(arr,eleIndex):
    n=len(arr)
    if eleIndex==n: return arr
    j=eleIndex-1
    key=arr[eleIndex]
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    return recurInsertionSort(arr,eleIndex+1)

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(recurInsertionSort(array,1))