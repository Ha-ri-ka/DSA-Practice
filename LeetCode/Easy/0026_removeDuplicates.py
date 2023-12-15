class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0        
        nextUnique=1
        for i in range(1,len(nums)):
            if (nums[i]!=nums[nextUnique-1]):
               nums[nextUnique]=nums[i]
               nextUnique+=1
        return nextUnique
    
