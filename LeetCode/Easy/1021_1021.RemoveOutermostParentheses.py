class Solution(object):
    def removeOuterParentheses(self, s):
        stack=[]
        counter=0
        ans=""
        for bracket in s:
            stack.append(bracket)
            if bracket=='(':
                counter+=1
            if bracket==")":
                counter-=1
            if counter==0:
                for s in stack[1:-1]:
                    ans+=s
                stack=[]
        return ans      
