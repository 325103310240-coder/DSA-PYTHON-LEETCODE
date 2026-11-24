class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=list(str(n))
        sum=0
        for i in range(0,len(n),2):
            sum=sum+int(n[i])
        for j in range(1,len(n),2):
            sum=sum-int(n[j])
        return sum
    

        


        
