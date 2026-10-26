class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        r1=[]
        r2=[]
        r3=[]
        for i in range(0,n):
            r1.append(nums[i])
        x=r1
        for j in range(n,len(nums)):
            r2.append(nums[j])
        y=r2
        for i in range(0,len(x)):
            for j in range(0,len(y)):
                if i==j:
    
                    r3.append(x[i])
                    r3.append(y[i])
                else:
                    continue
                
            
        return r3
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

        
