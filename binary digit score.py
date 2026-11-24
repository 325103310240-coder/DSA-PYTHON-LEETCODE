class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a=bin(a)[2:]
        s1=0
        s2=0
        b=bin(b)[2:]
        a=list(str(a))
        b=list(str(b))
        for i in range(len(a)):
            if a[i]=='1':
                s1+=1
            else:
                s1+=0
        for j in range(len(b)):
            if b[j]=='1':
                s2+=1
            else:
                s2+=0
        if s1>=s2:
            return s1*s2
        else:
            return s2/s1
                
        
