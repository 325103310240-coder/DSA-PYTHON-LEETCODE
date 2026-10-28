class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        words=s.split()
        for word in words:
            l.append(word[::-1])
        return (" ".join(l))
        
    : s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
