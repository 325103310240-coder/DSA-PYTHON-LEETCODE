class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
        res=[]
        res1=[]
        res2=[]
        for i in range(0,len(nums)):
            if nums[i]==pivot:
                res2.append(nums[i])
            elif(nums[i]<pivot):
                res1.append(nums[i])
            else:
                res.append(nums[i])
        return res1+res2+res



        
Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
Example 2:
