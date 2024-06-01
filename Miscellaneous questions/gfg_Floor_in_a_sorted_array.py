    def findFloor(self,A,N,X):
        #Your code here
        start,end=0,N-1
        while(start<=end):
            mid=(start+end)//2
            if A[mid]==X:
                return mid
            if X<A[mid]:
                end=mid-1
            elif X>A[mid]:
                start=mid+1
        if X<A[mid]:
            return mid-1
        if X>A[mid]:
            return mid
        return -1
