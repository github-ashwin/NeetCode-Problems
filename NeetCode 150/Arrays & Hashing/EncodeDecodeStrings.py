from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Length of the string + delimiter + string
        enc = ""
        for string in strs:
            length = len(string)
            enc+=str(length)+"^"+string
        return enc
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '^':
                j +=1
            str_len = int(s[i:j])
            start = j+1
            end = start + str_len
            result.append(s[start:end])
            i = end
        return result
        
