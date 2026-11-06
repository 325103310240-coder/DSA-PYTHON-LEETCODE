class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n<4 and n!=2) or n%2!=0 :
            return False
        a=0
        b=1

        while True:
            c=(a+b)
            if(2*c)==n:
                return True
            if(2*c)>n:
                return False
            a=b
            b=c
            

    
        

        
