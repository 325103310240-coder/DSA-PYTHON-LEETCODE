class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[] 
        for i in range(len(nums)):
            if nums[i]>1:
                prime=True
            
                for j in range(2,nums[i]):
                    if (nums[i]%j)==0:
                        prime=False
                        break
                if prime:
                    arr.append(i)
        
        return ((arr[-1])-(arr[0]))

        
