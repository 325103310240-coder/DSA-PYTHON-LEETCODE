class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        
        n=len(temperatures)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            st.append(i)
        return res





        
