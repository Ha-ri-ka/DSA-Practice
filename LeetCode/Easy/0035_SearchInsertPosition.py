class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        start,end=0,n-1
        while(start<=end):
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
        # print(nums[mid])
        if target<nums[mid]:
            return mid
        if target>nums[mid]:
            return mid+1
        
