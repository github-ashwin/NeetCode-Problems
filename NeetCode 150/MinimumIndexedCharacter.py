class Solution:
    def minIndexChar(self,s1,s2): 
        #code here
        present = set(s2)
        
        for i, ch in enumerate(s1):
            if ch in present:
                return i
        
        return -1
