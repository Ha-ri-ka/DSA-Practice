class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        index=0
        for i in range(n):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,n):
            nums[i]=0
