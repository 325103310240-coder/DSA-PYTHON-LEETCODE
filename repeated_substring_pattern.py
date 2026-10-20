Check whether a string can be formed by repeating one of its substrings multiple times.

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        y=s[0]
    
        for i in range(1,len(s)):
            if s[i] ==y:
  
                z=s[0:i]
                

    
                a=len(z)
                if len(s)%a!=0:
                    continue
                count=0
                for j in range(a,len(s),a):
                    c=s[j:j+a]

                    if c!=z:
                        count+=1
                    else:
                        count+=0
                if count==0:
                    return True
        return False

