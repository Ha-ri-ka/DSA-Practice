class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        if n==0: return [-1,-1]
        start,end=0,n-1
        indices=[]
        found=0
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                found=1
                break
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
        if(found):
            while (start<=mid and nums[start]!=target):
                start+=1
            while (end>=mid and nums[end]!=target):
                end-=1
            return [start,end]
        return [-1,-1]        
