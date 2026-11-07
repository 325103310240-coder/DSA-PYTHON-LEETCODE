You are given an integer array nums of length n.

An index i is called a peak if all of the following conditions hold:

0 < i < n - 1
nums[i] > nums[i - 1]
nums[i] > nums[i + 1]
An index i is called a valley if all of the following conditions hold:

0 < i < n - 1
nums[i] < nums[i - 1]
nums[i] < nums[i + 1]
Return an integer denoting the difference between the sum of all peak values and the sum of all valley values.

 

Example 1:

Input: nums = [1,5,2,4,1,3,0]

Output: 9

Explanation:

The peak values are nums[1] = 5, nums[3] = 4, and nums[5] = 3.
The valley values are nums[2] = 2 and nums[4] = 1.
The difference between the sum of the peak values and the sum of the valley values is (5 + 4 + 3) - (2 + 1) = 9. Hence, the answer is 9.
class Solution(object):
    def peakValleyDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1=[]
        res2=[]
        for i in range(1,len(nums)-1):
            if(nums[i]>nums[i-1]) and (nums[i]>nums[i+1]):
                res1.append(nums[i])
            elif(nums[i]<nums[i-1]) and (nums[i]<nums[i+1]):
                res2.append(nums[i])
            else:
                continue
        x=sum(res1)
        y=sum(res2)
        return (x-y)
                
        
