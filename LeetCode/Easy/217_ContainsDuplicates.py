class Solution(object):
    def containsDuplicate(self, nums):
        #for i in range(len(nums)):
        #   if nums[i] in nums[i+1:]:
        #      return True
        #return False
        #unique=set(nums)
        if len(set(nums))==len(nums):
            return False
        return True
