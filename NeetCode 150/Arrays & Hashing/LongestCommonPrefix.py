from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        
        common = strs[0]

        for i in range(1,len(strs)):
            current = strs[i]

            # Finding the common prefix
            while not current.startswith(common):
                common = common[:-1] # Remove last character
                if not common:
                    return ""
                    
        return common

        