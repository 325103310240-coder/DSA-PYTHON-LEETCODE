class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        b=[]
        n=list(str(n))
        for i in range(len(n)):
            count=1
            if int(n[i]) not in a:
                a.append(int(n[i]))
                for j in range(i+1,len(n)):
                    if int(n[i])==int(n[j]):
                        count+=1
            else:
                continue
            b.append(count*int(n[i]))
        return sum(b)
                    
