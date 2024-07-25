class Solution(object):
    def generate(self, numRows):
        triangle=[[1]]
        if numRows==1: return triangle
        triangle=[[1],[1,1]]
        if numRows==2: return triangle
        for i in range(2,numRows):
            row=[1]
            prev=triangle[i-1]
            for j in range(len(prev)-1):
                ele=prev[j]+prev[j+1]
                row.append(ele)
            row.append(1)
            triangle.append(row)
        return triangle


        
