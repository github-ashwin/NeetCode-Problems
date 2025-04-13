class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def encode(word):
            mapping = {}
            result = []
            for c in word:
                if c not in mapping:
                    mapping[c] = len(mapping)
                result.append(mapping[c])
            return result

        p = encode(pattern)
        res = []
        for w in words:
            if encode(w) == p:
                res.append(w)
        return res