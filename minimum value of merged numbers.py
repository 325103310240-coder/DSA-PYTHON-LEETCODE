class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1=[]
        
        for i in range(0,len(nums)-1,2):
            res=[]
            j=i+1
            res.append(nums[i])
            res.append(nums[j])
        
            x=int(''.join(map(str,res)))
            x1.append(x)
        min=x1[0]
        for i in range(len(x1)):
            if (x1[i]<min):
                min=x1[i]
        return min
            
        
        
