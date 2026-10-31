class Solution(object):
    def fib(self, n):

        """
        :type n: int
        :rtype: int
    """
        def fibi(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return fibi(n-1)+fibi(n-2)
        return fibi(n)


        
