class Solution:
    def kthElement(self, a, b, k):
        # code here
        len1 = len(a)
        len2 = len(b)
        
        if len1 > len2:
            return self.kthElement(b, a, k)
        
        low = max(0, k - len2)  # if b is small
        high = min(k, len1)     # limiting the remaining elements
        
        while low <= high:
            part_a = (low + high) // 2
            part_b = k - part_a  
            
            l1 = a[part_a - 1] if part_a > 0 else float('-inf')
            l2 = b[part_b - 1] if part_b > 0 else float('-inf')
            
            r1 = a[part_a] if part_a < len1 else float('inf')
            r2 = b[part_b] if part_b < len2 else float('inf')
            
            # maximum of left part < minimum of right part
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = part_a - 1
            else:
                low = part_a + 1
        return -1
