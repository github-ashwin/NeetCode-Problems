from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                result[prev_index] = index - prev_index
            stack.append((temp, index))
        
        return result
