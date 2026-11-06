class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in  nums:
            maxi=max(nums)
            if i==maxi:
                continue
            else:
                while i!=maxi:
                    i+=1
                    count+=1
        return count

        
