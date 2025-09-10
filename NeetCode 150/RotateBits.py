#User function Template for python3

class Solution:
    def rotate(self, n, d):
        # code here
        d = d % 16
        
        # Left rotation: wrap into 16-bit
        left = ((n << d) | (n >> (16 - d))) & 0xFFFF
        
        # Right rotation: for N >= 2^16, keep original number if D % 16 == 0
        if d == 0:
            right = n
        else:
            right = ((n >> d) | (n << (16 - d))) & 0xFFFF
        
        return [left, right]
