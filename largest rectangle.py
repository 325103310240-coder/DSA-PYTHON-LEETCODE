class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        st=[]
    
        for i in range(0,len(prices)):
            found=False
            for j in range(i+1,len(prices)):
                
                

                if prices[j]<=prices[i]:
                    st.append(prices[i]-prices[j])
                    found=True
                    break
                else:
                    continue
            if found==False:
                

                st.append(prices[i])
        return st
        

        
