class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        length = 0
        n = len(s)

        for i in range(n):
            # Check for odd-length palindrome (center at i)
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                # Check if the new palindrome is longer
                if (right - left + 1) > length:
                    result = s[left:right + 1]
                    length = right - left + 1
                left -= 1
                right += 1

            # Check for even-length palindrome (center at i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                # Check if the new palindrome is longer
                if (right - left + 1) > length:
                    result = s[left:right + 1]
                    length = right - left + 1
                left -= 1
                right += 1

        return result
