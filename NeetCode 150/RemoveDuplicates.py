class Solution:
    def removeDups(self, s):
        # code here
        seen = set()
        result = ""
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result += ch
        
        return result
