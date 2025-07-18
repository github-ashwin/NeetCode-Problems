from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        one_step,two_step=1,1
        
        for i in range(n-1):
            temp = one_step
            one_step = one_step + two_step
            two_step = temp
        
        return one_step
        