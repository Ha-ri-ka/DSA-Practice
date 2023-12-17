class Solution(object):
    #solution 0
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        zeroIndices=[]
        zeroIndices.append(-1)
        for i in range (n):
            if nums[i]==0:
                zeroIndices.append(i)
        zeroIndices.append(n)
        print(zeroIndices)
        maxDiff=0
        for i in range(len(zeroIndices)-1):
            diff=zeroIndices[i+1]-zeroIndices[i]
            if diff>maxDiff:
                maxDiff=diff
        return maxDiff-1        
