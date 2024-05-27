class Solution(object):
    def longestConsecutive(self, nums):
    #------O(nlogN)+O(n)----------------#
        # nums=sorted(nums)
        # if len(nums)==0: 
        #     return 0
        # seqLen=1
        # maxLen=1
        # for i in range(len(nums)-1):
        #     if nums[i+1]==nums[i]+1:
        #         seqLen+=1
        #     elif nums[i]==nums[i+1]:
        #         continue
        #     else:
        #         seqLen=1
        #     maxLen=max(maxLen,seqLen)
        # return maxLen
    #-----------O(n)---------------------#
        n=len(nums)
        if n==0:
            return 0
        numsSet=set()
        for num in nums:
            numsSet.add(num)
        maxLen,seqLen=1,1
        for num in numsSet:
            seqLen=1
            if num-1 not in numsSet:
                curr=num
                while curr+1 in numsSet:
                    seqLen+=1
                    curr+=1
            maxLen=max(seqLen,maxLen)
        return maxLen        
