class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        count=0
        
        for i in range(0,len(s)):
            vowels=0
            consonants=0
            for j in range(i,len(s)):

                if s[j] in 'aeiou':
                
                    vowels+=1
                else:
                    consonants+=1
                if vowels==consonants and ((vowels*consonants)%k)==0:
                    count+=1
                else:
                    continue
        return count
                



        
