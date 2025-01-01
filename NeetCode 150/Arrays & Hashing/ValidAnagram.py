class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        ds = {}
        dt = {}
        for i in slist:
            if i in ds:
                ds[i] = ds[i]+1
            else:
                ds[i] = 1
        
        for j in tlist:
            if j in dt:
                dt[j] = dt[j] + 1
            else:
                dt[j] = 1
        
        if ds==dt:
            return True
        else:
            return False

# Alternate Approach

# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Quick length check
#         if len(s) != len(t):
#             return False
        
#         # Use Counter to compare character frequencies
#         return Counter(s) == Counter(t)
