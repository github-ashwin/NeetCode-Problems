class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordmap = {} 

        for s in strs:
            key = "".join(sorted(s))
            if key not in wordmap:
                wordmap[key] = []
            wordmap[key].append(s)

        return list(wordmap.values())

        