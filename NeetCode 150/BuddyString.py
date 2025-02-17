class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) == 2:
            i, j = diff
            return s[i] == goal[j] and s[j] == goal[i]
        
        return False
