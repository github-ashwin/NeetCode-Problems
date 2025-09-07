class Solution:
    def areAnagrams(self, s1, s2):
        # code here
        
        # helper function
        def hm(string):
            hashmap = {}
            for char in string:
                hashmap[char] = hashmap.get(char, 0) + 1
            return hashmap

        return hm(s1) == hm(s2)
