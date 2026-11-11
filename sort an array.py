class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def merge(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left_half=nums[:mid]
                right_half=nums[mid:]
                merge(left_half)
                merge(right_half)
                i=j=k=0
                while i<len(left_half) and j<len(right_half):
                    if left_half[i]<right_half[j]:
                        nums[k]=left_half[i]
                        i+=1
                    else:
                        nums[k]=right_half[j]
                        j+=1
                    k+=1
                while i<len(left_half):
                    nums[k]=left_half[i]
                    i+=1
                    k+=1
                while j<len(right_half):
                    nums[k]=right_half[j]
                    j+=1
                    k+=1
        merge(nums)
        return nums
        
