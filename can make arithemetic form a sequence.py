class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        ar=[]
    
        for i in range(0,len(arr)-1):
            j=i+1
            k=abs(arr[i]-arr[j])
            if k in ar:
                continue
            else:
                ar.append(k)
        if len(ar)==1:
            return True
        else:
            return False

            

        
