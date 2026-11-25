class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        b=[]
        nums.sort()
        for i in range(len(nums)):
            count=1
            if nums[i] not in a:
                for j in range(i+1,len(nums)):
                    if nums[i]==nums[j]:
                        count+=1
            else:
                continue
            a[nums[i]]=count
        for key,val in a.items():

            if val==1:
                return key
        
                
                
        
        
            

        
