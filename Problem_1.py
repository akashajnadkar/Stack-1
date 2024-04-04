'''
Time Complexity - O(2n). We are traversing the array twice
Space Complexity - O(n). We are using stack.
'''
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        tempStack = deque()
        for i in range(len(temperatures)):
            #if the current teperature is higher than that on top of stack
            while tempStack and temperatures[i] > temperatures[tempStack[-1]]:
                lowerTemp = tempStack.pop()
                result[lowerTemp] = i - lowerTemp
            #push the current index onto the stack 
            tempStack.append(i)
        return result
        