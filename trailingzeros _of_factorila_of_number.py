class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        count=0
        x=str(fact)
        for digit in x[::-1]:
            if digit=='0':
                count+=1
            else:
                break
        return count
