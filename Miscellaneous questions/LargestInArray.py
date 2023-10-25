def findLargest(array):
    large=array[0]
    for ele in array:
        if ele>large:
            large=ele
    return large
  

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(findLargest(array))
