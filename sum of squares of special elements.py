class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum=0
        for i in range(0,n):
            if (n%(i+1))==0:
                sum=sum+(nums[i]*nums[i])
            else:
                continue
        return sum
        

        
