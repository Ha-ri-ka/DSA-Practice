def checkSorted(array,len):
    for i in range(0,len-1):
        if array[i]>array[i+1]:
            return False
    return True

n=int(input("Enter length of array:"))
array=[]
for i in range(n):
    ele=int(input(f"array[{i}]="))
    array.append(ele)
if(checkSorted(array,n)):
    print("It is a sorted array.")
else:
    print("it is NOT a sorted array.")
