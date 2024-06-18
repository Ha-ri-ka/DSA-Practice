class Solution(object):
    def setZeroes(self, matrix):
        #brute force----------------------------
        # indices=[]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             indices.append((i,j))
        # for index in indices:
        #     row=index[0]
        #     for c in range(len(matrix[0])):
        #         matrix[row][c]=0
        #     col=index[1]
        #     for r in range(len(matrix)):
        #         matrix[r][col]=0


        #optimal----------------------------------
        # row0,col0=False,False
        # n=len(matrix)
        # m=len(matrix[0])
        # for i in range(n):
        #     for j in range(m):
        #         if i==0:
        #             if matrix[0][j]==0:
        #                 row0=True
        #         if j==0:
        #             if matrix[i][0]==0:
        #                 col0=True
        #         if matrix[i][j]==0:
        #             matrix[0][j]=0
        #             matrix[i][0]=0
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][0]==0 or matrix[0][j]==0:
        #             matrix[i][j]=0
        # if row0:
        #     for i in range(m):
        #         matrix[0][i]=0
        # if col0:
        #     for i in range(n):
        #         matrix[i][0]=0

        
        #----trying again
        r=len(matrix)
        c=len(matrix[0])
        cols=[]
        rows=[]
        for i in range (r):
            for j in range (c):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        for row in rows:
                for j in range(c):
                    matrix[row][j]=0
        for col in cols:
            for i in range(r):
                    matrix[i][col]=0

        
