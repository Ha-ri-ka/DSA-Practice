class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low,high=0,n-1
        if n==1:
            if nums[0]==target: return 0
            return -1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]: #left part of array is sorted
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else: #right part of array is sorted
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1      
