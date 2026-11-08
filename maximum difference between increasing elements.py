class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]<nums[j]):
                    res.append((nums[j]-nums[i]))
                else:
                    continue
        if len(res)==0:
            return -1
        else:
            return max(res)
        
