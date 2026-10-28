class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        
        res=[]
        
        for i in range(0,len(s)):
            if('a'<=s[i]<='z' or '0'<=s[i]<='9'):
                res.append(s[i])
                
            else:
                continue
        y="".join(res)
        x=y[::-1]
        if x==y:
            return True
        else:
            return False

            
        Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
