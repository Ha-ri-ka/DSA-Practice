def recurBubbleSort(arr,passNum):
    n=len(arr)
    swapped=False
    if passNum==n-1: return arr
    for j in range(n-passNum-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if swapped==False: return arr
    return recurBubbleSort(arr,passNum+1)


array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(recurBubbleSort(array,0))