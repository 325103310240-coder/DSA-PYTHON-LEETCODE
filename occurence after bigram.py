Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text=text.split()
        ar=[]
        for i in range(len(text)-2):
            if text[i]==first and text[i+1]==second:
                ar.append(text[i+2])
        return ar
                
        
