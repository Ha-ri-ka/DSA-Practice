class Solution(object):
    def searchInsert(self,nums,target):
        s,e=0,len(nums)-1
        while s<=e:
            m=(s+e)//2
            if nums[m]==target: return m
            if nums[m]>target: e=m-1
            elif nums[m]<target: s=m+1
        if nums[m]<target: return m+1
        if nums[m]>target: return m
