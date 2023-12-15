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

    #solution 3: list slicing
    def rotate(self, nums, k):
        n=len(nums)
        flag=True
        if k > n:
            k=k-n
        if k==n or n==0 or n==1 or k==0:
            flag=False
        if(flag):
            if(n==2):
                nums.reverse()
            elif(n>2):
                nums.reverse()
                nums[:k]=reversed(nums[:k])
                nums[k:]=reversed(nums[k:])       
