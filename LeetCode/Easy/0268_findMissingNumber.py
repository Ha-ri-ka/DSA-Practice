class Solution(object):
  #solution 1: O(n2)
    def missingNumber(self, nums):
        n=len(nums)
        flag=0
        for i in range(n):
            if i not in nums:
                flag=1
                break
        if(flag==0): return n 
        return i        
      
      #solution 2: O(n)
        def missingNumber(self, nums):
            n=len(nums)
            if(n==0):
              return n
            expectedSum=n*(n+1)//2
            arraySum=sum(nums)
            return expectedSum-arraySum
