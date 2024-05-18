class Solution:
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        leaders=[]
        leaders.append(A[N-1])
        maxEle=A[N-1]
        for i in range(N-2,-1,-1):
            if A[i]>=maxEle:
                maxEle=A[i]
                leaders.append(maxEle)
        leaders.reverse()
        return (leaders)
