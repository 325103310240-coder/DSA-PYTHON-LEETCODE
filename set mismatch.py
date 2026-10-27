class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        nums.sort()
        mid=(len(nums)/2)
        for i in range(0,len(nums)-1):
            j=i+1
            if nums[i]==nums[j]:
                res.append(nums[i])
            else:
                continue
            
        
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
            

        return res
                    
Input: nums = [1,2,2,4]
Output: [2,3]

        
        
            
                
        return res
        
