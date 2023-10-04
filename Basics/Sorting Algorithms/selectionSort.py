def selectionSort(array):
    n=len(array)
    for i in range (n-1):
        for j in range(i,n):
            if(array[j]<array[i]):
                array[j],array[i]=array[i],array[j]
    return array

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(selectionSort(array))
