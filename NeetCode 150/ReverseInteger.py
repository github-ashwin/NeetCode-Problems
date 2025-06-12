class Solution:
    def reverse(self, x: int) -> int:
        min_lim = -2**31
        max_lim = (2**31)-1

        result = 0

        sign = 1 if x >= 0 else -1

        x = abs(x)
        while x!=0:
            d = x%10
            x//=10

            if result > (max_lim - d)//10:
                return 0
            result = result*10 + d
        return result*sign
