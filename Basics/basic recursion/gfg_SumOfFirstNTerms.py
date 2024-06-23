class Solution:
    def sumOfSeries(self,n):
        #if(n==1):
        #    return 1
        #return (n**3)+self.sumOfSeries(n-1)
        
        #to avoid maximum recursion depth exceeded error, we use formula instead of recursion
        return (n * (n + 1) // 2) ** 2
