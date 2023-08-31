class Solution(object):
    def plusOne(self, digits):
        if (len(digits)==0): return None
        if(digits[len(digits)-1]!=9):
            digits[len(digits)-1]+=1
            return digits
        ans=[]
        carry=1
        for i in range(len(digits)-1,-1,-1):
            sum=digits[i]+carry
            ans.append(sum%10)
            carry=sum//10
            if(i==0 and carry==1): ans.append(carry)
        ans.reverse()
        return(ans)
