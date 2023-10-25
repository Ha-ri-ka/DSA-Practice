def secondLargest(array): #complexty: O(n^2)
    large=array[0]
    secondLarge=-1
    for ele in array:
        if ele>large:
            large=ele
    for ele in array:
        if ele > secondLarge and ele!=large:
            secondLarge=ele
    return secondLarge

def secondLargestSinglePass(array): #complexity: O(n)
    large,secondLarge=float('-inf'),float('-inf')
    for ele in array:
        if ele>large:
            secondLarge=large
            large=ele
        elif ele>secondLarge and ele!=large:
            secondLarge=ele
    return secondLarge
  

array=[]
n=int(input("enter length of array:"))
for i in range (n):
    array.append(int(input("element: ")))
print(array)
print(secondLargest(array))
print(secondLargestSinglePass(array))
