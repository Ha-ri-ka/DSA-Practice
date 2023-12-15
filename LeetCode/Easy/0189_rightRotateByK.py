class Solution(object):
    #solution 1
    def rotate(self, nums, k): #time limit exceeded 
        n=len(nums)
        for i in range (k):
            ele=nums.pop(n-1)
            nums.insert(0,ele)

      
    #solution 2: circular increment
    def rotate(self, nums, k):
        n=len(nums)
        temp=list(nums)
        for i in range (n):
            nums[(i+k)%(n)]=temp[i]
        
  
