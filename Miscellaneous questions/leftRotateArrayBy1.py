def leftRotate(nums):
    ele=nums.pop(0)
    nums.append(ele)
    return nums
n=int(input("Length of array:"))
nums=[]
for i in range(n):
    ele=int(input(f"array[{i}]="))
    nums.append(ele)
print(f"before rotate:{nums}")
print(f"after rotate:{leftRotate(nums)}")
