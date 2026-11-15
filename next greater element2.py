Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        n=len(nums)
    
        res=[-1]*n
        for i in range(n-1,-1,-1):
            found=False
            for j in range(i,n):
                if nums[j]>nums[i]:
                    res[i]=nums[j]
                    found=True
                    break
                else:
                    continue
            if found==False:              
                for j in range(0,i):
                    if nums[j]>nums[i]:
                        res[i]=(nums[j])
                        break
                    else:
                        continue
        return res

                    
        
        
