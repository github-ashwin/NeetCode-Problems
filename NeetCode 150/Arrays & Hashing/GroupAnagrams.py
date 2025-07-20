from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Hashmap to group anagrams

        for s in strs:
            count = [0] * 26  # Frequency of each letter in the word

            for char in s:
                count[ord(char) - ord('a')] += 1  # Count characters

            anagram_map[tuple(count)].append(s)  # Use tuple as key

        return list(anagram_map.values())  # Convert dict_values to list
