class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i=0
        while i<len(s):
            j=0
            found=False
            while j<len(t):
                if s[i]==t[j]:
                    s=s[:i]+s[i+1:]
                    t=t[:j]+t[j+1:]
                    found=True
                    break
                j+=1
            if not found:
                i+=1
        return t

        
