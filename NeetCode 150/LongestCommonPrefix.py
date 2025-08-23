#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        
        prefix = arr[0]
        
        for word in arr[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
        return prefix
            
