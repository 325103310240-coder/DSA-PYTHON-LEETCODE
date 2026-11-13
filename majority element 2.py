class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        count=1
        ar=[]
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                count=1
            if count>len(nums)//3:
                ar.append(nums[i])
        return list(set(ar))

        
