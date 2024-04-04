'''
Time Complexity - O(3n). 2 times traversal of array as circular array
Space Complexity - O(n). We are using stack

Works on Leetcode
'''
from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        result = [-1] * len(nums)
        for i in range(2*len(nums)):
            #current number is greater than that of top
            while stack and nums[i%len(nums)] > nums[stack[-1]]:
                lower = stack.pop()
                result[lower] = nums[i%len(nums)]               
            if i<len(nums):
                stack.append(i)
        return result
