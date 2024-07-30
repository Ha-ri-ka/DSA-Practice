class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2: 
            return [0,1]
        n=len(nums)
        #brute force----------------
        # for i in range(n):
        #     ele=nums[i]
        #     for j in range(i+1,len(nums)):
        #         ans=0
        #         ans=ele+nums[j]
        #         if ans==target:
        #             return [i,j]

        # optimal---------------------
        indicesMap={}
        for i in range(n):
            indicesMap[nums[i]]=i
        print(indicesMap)   
        for i in range(n):
            ele2=target-nums[i]
            if ele2 in indicesMap and indicesMap[ele2]!=i:
                return [i,indicesMap[ele2]] 
