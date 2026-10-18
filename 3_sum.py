# LeetCode 3Sum – Python

## Problem Description
Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` such that:

`nums[i] + nums[j] + nums[k] == 0`

The solution must not contain duplicate triplets.

## Approach
1. Use three nested loops to select three different elements.
2. Check whether their sum equals zero.
3. Sort each valid triplet to keep its elements in a consistent order.
4. Check whether the triplet is already in the result list.
5. Add only unique triplets to the result.
6. Return the list of triplets.

## Python Solution

```python
class Solution(object):
    def threeSum(self, nums):
        result = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted(
                            [nums[i], nums[j], nums[k]]
                        )

                        if triplet not in result:
                            result.append(triplet)

        return result
```

## Example

**Input**
```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output**
```python
[[-1, -1, 2], [-1, 0, 1]]
```

## Concepts Used
- Python classes and methods
- Lists and nested lists
- Nested `for` loops
- Conditional statements
- List indexing
- The `sorted()` function
- The `append()` method
- Duplicate checking

## What I Learned
- How to use a class and method to organize a coding solution.
- How to use three nested loops to check combinations of array elements.
- How to find triplets whose sum equals zero.
- How to sort a list and avoid duplicate triplets.
- Why `return` must be placed outside the loops when collecting multiple results.
- How to debug Python errors and improve problem-solving skills.

## Complexity Analysis
- **Time Complexity:** O(n³) for checking triplets, excluding the additional overhead of sorting and duplicate checking.
- **Space Complexity:** Depends on the number of unique triplets stored, plus temporary storage for each triplet.

## Future Improvement
I plan to optimize this solution using the two-pointer technique to reduce the time complexity to O(n²).
