def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    finalArray=[]
    i,j=0,0
    while(i<n1 and j<n2):
        if arr1[i]<arr2[j]:
            finalArray.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            finalArray.append(arr2[j])
            j+=1
        elif arr1[i]==arr2[j]:
            finalArray.append(arr1[i])
            i+=1
            j+=1
    if (i==n1):
        while(j<=n2-1):
            finalArray.append(arr2[j])
            j+=1
    else:
        while(i<=n1-1):
            finalArray.append(arr1[i])
            i+=1
    return finalArray

n1=int(input('Length of array 1:'))
arr1=[]
for i in range(n1):
    ele=int(input(f'array[{i}]='))
    arr1.append(ele)

n2=int(input('Length of array 2:'))
arr2=[]
for i in range(n2):
    ele=int(input(f'array[{i}]='))
    arr2.append(ele)
print(f"sorted array 1: {sorted(arr1)}")
print(f"sorted array 2: {sorted(arr2)}")
print(f"sorted union of the arrays: {union(sorted(arr1),sorted(arr2))}")
