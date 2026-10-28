class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]

        for i in range(0,len(matrix)):
            count=0
            for j in range(0,len(matrix)):

                if matrix[i][j]==1:
                    count+=1
                else:
                    count+=0
            res.append(count)
        return res
    Example 1:



Input: matrix = [[0,1,1],[1,0,1],[1,1,0]]

Output: [2,2,2]

Explanation:

Vertex 0 is connected to vertices 1 and 2, so its degree is 2.
Vertex 1 is connected to vertices 0 and 2, so its degree is 2.
Vertex 2 is connected to vertices 0 and 1, so its degree is 2.
Thus, the answer is [2, 2, 2].


        
        
