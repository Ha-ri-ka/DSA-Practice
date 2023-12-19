class Solution(object):
    #solution 0:    
    def twoSum(self, nums, target):
        indices=[]
        n=len(nums)
        for i in range(n):
            Twosum=0
            Twosum+=nums[i]
            for j in range (i+1,n):
                if (Twosum+nums[j]==target):
                    indices.append(i)
                    indices.append(j)
        return indices      
