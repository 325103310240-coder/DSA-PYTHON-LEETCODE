Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range(0,len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,len(nums)-1):
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    for l in range(k+1,len(nums)):
                        if l>k+1 and nums[l]==nums[l-1]:
                            continue
                        
                        total = nums[i]+nums[j]+nums[k]+nums[l]
                        if total==target:
                            result.append([nums[i],nums[j],nums[k],nums[l]])
                        elif total>target:
                            break
                        
        return result
                                
        
        
