def insertionSort(array):
    n=len(array)
    for i in range(1,n):
        j=i-1
        key=array[i]
        while(key<array[j] and j>=0):
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return(array)

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(insertionSort(array))    