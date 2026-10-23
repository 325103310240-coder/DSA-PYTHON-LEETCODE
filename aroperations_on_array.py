# LeetCode 2460 – Apply Operations to an Array

## Problem
Given an integer array `nums`, apply operations to adjacent elements. If two consecutive elements are equal, double the first element and set the second element to `0`. After completing all operations, move all zeros to the end of the array.

## Approach
I solved this problem using Python by following these steps:

1. **Apply operations:** Iterate through the array and compare each element with the next element.
2. **Update elements:** If two adjacent elements are equal, double the current element and replace the next element with `0`.
3. **Count zeros:** Count the number of zeros after completing all operations.
4. **Move zeros:** Use a list comprehension to collect all nonzero elements, then append the required number of zeros.
5. **Return the result:** Return the modified array.

## Python Concepts Used
- `for` loops
- `if` conditions
- List indexing
- List comprehensions
- `count()` and list operations

## Example

**Input:**
```python
nums = [1, 2, 2, 1, 1, 0]
```

**Output:**
```python
[1, 4, 2, 0, 0, 0]
```

## What I Learned
- How to process adjacent elements in an array.
- How sequential operations affect later comparisons.
- How to move all zeros to the end while preserving the order of nonzero elements.
- How to combine loops and list comprehensions to solve array problems.

## Complexity Analysis
- **Time Complexity:** `O(n)`, where `n` is the length of the array.
- **Space Complexity:** `O(n)` for creating the resulting list.

## Platform
LeetCode – Problem 2460 (Easy)

Problem link: https://leetcode.com/problems/apply-operations-to-an-array/
#solution
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            else:
                continue
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        zeros=count
        nums=[x for x in nums if x!=0]+[0]*zeros
        return nums
        
