def mergeSort(array,low,high):
    if(low >= high): return
    mid=(low+high)//2
    mergeSort(array,low,mid)
    # print(array[low:high])
    mergeSort(array,mid+1,high)
    # print(array[low:high])
    merge(array,low,mid,high)
    # print(array)

def merge(array,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(array[left] <= array[right]):
            temp.append(array[left])
            left+=1
        else:
            temp.append(array[right])
            right+=1
    while(left <=mid):
        temp.append(array[left])
        left+=1
    while(right<=high):
        temp.append(array[right])
        right+=1
    for i in range (low,high+1):
        array[i]=temp[i-low]

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(mergeSort(array,0,n-1))
