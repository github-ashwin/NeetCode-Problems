from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc+= str(len(i))+'/'+i #length of the string,delimiter,string
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0

        while i<len(s):
            j = i
            while s[j] != '/':
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            dec.append(s[i:j])
            i = j
        
        return dec
