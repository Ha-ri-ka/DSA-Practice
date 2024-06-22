class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        #using dictionary--------------
        #hashMap={}
        #for i in range (1,N+1):
        #    hashMap[i]=0
        #for num in arr:
        #    if num<=N:
        #        hashMap[num]+=1
        #i=0
        #for k in hashMap.values():
        #    arr[i]=k
        #    i+=1
        
        #using another array--------------
        freq=[0] * (N+1)
        for num in arr:
            if num<=N:
                freq[num]+=1
        arr[:]=freq[1:]
