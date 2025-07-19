# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         slist = list(s)
#         tlist = list(t)
#         ds = {}
#         dt = {}
#         for i in slist:
#             if i in ds:
#                 ds[i] = ds[i]+1
#             else:
#                 ds[i] = 1
        
#         for j in tlist:
#             if j in dt:
#                 dt[j] = dt[j] + 1
#             else:
#                 dt[j] = 1
        
#         if ds==dt:
#             return True
#         else:
#             return False

from collections import Counter
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If length mismatch, not an anagram
        if len(s) != len(t):
            return False
        
        # Counter is used to find hashtable objects
        return Counter(s) == Counter(t)

