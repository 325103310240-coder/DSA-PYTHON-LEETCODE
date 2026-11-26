class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n=list(str(n))
        found=0
        if int(n[0])==x:
            return False
        else:

            for i in range(0,len(n)):
                if int(n[i])==x:
                    
                    found=1
                    break
                else:
                    continue
            if found==1:

                return True
            else:
                return False

        
