def bubbleSort(array):
    n=len(array)
    i=0
    for iter in range (n-1): #0 to n-2 = n-1 iterations
        for i in range (n-i-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
    return(array)

def optimizedBubbleSort(array):
    n=len(array)
    i=0
    for iter in range (n-1): #0 to n-2 = n-1 iterations
        swapped=False
        for i in range (n-i-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                swapped=True
        if (swapped==False): #if after any of the iteration no swaps take place, the array is sorted.
            break 
    return(array)


array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(bubbleSort(array))
