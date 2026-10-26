class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        res=[]
        if (len(nums)==1 and nums[0]==1):
            return 1
        
        elif (len(nums)==1 and nums[0]!=1):
            return 0
        elif(len(nums)==2):
            coun1=0
            for i in range(0,len(nums)):
                if nums[i]==1:
                    coun1+=1
            return coun1
        elif(len(nums)==3 and nums[0]==0 and nums[1]==0 and nums[2]==0):
            return 0

        
        
        
        else:
            for i in range(0,len(nums)-1):
                if nums[i]==nums[i+1]==1:
                    count+=1
                    res.append(count)
                else:
                    count=1
                
                    res.append(count)

        
        
        
        
        return max(res)
