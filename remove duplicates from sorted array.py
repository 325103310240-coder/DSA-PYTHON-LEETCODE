class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in nums:
            if i  not in res:
                res.append(i)

        
        
        
        for i in range(0,len(res)):
            nums[i]=res[i]
        return len(res)

        

            



        
        
