#User function Template for python3

class Solution:
    def allPairs(self, target, arr1, arr2):
        # Your code goes here
        freq = {}
        for num in arr2:
            freq[num] = freq.get(num, 0) + 1
        
        result = []

        for num in arr1:
            complement = target - num
            if complement in freq:
                
                for _ in range(freq[complement]):
                    result.append((num, complement))
        
        
        return sorted(result)
