class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        start,end=0,n-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
        return -1       
