class Solution(object):
    def check(self, nums):
        n=len(nums)
        temp=sorted(nums)
        if nums==temp:
            return True
        for i in range (1,n):
            ele=nums.pop(0)
            nums.append(ele)
            if nums==temp:
                return True
        return False
