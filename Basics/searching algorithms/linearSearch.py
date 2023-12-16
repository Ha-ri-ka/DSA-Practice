def linearSearch(nums,key):
    n=len(nums)
    for i in range(n):
        if nums[i]==key:
            return i
    return -1  
