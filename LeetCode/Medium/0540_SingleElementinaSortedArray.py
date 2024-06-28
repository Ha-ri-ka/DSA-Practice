class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        if nums[0]!=nums[1]: return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]: return nums[len(nums)-1]
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            # if you are at an odd index
            if mid%2==1:
                #if its duplicate is the number AFTER it
                if nums[mid]==nums[mid+1]:
                    #then the single element is to the left of current index
                    end=mid-1 #eliminate the right
                #if its duplicate is the number BEFORE it
                elif nums[mid]==nums[mid-1]:
                    start=mid+1
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    start=mid+1
                if nums[mid]==nums[mid-1]:
                    end=mid-1
            
        
