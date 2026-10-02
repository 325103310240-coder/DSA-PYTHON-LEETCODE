#Leetcode-Two Sum
#given an array and a target,fns two numbers whose sum equal the target
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
