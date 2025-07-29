class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f , s = 0,0 # Two pointers to keep track of the word length
        result = ""

        while f<len(word1) and s<len(word2):
            result +=word1[f]+word2[s]
            f+=1
            s+=1

        result += word1[f:] + word2[s:] # adding remaining words
        return result
            
        