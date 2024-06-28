import sys
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        mini=sys.maxsize
        while(start<=end):
            mid=(start+end)//2
            # left half is sorted
            if nums[start]<=nums[mid]:
                mini=min(mini,nums[start])
                start=mid+1
            #right half is sorted
            else:
                mini=min(mini,nums[mid])
                end=mid-1
        return mini
