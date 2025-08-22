# User function Template for python3
from collections import Counter
class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        # hashmap approach
        
        a_count = Counter(a)
        b_count = Counter(b)
        
        # print(a_count)
        
        for num in b_count:
            if num not in a_count or b_count[num] > a_count[num]:
                return False
        return True
    
    
    
