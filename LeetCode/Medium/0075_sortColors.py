class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        z,o,t=0,0,0
        i,j,k=0,0,0
        for num in nums:
            if num==0:
                z+=1
            if num==1:
                o+=1
            if num==2:
                t+=1
        pointer=0
        for i in range(z):
                nums[pointer]=0
                pointer+=1
        for j in range(o):
                nums[pointer]=1
                pointer+=1
        for k in range(t):
                nums[pointer]=2
                pointer+=1       
