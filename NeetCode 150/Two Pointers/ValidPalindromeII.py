class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1
                while l < r and not s[r].isalnum():
                    r -= 1
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s)-1

        while left <= right:
            while left<=right and not s[left].isalnum():
                left+=1
            while left<=right and not s[right].isalnum():
                right-=1
            
            if s[left].lower() != s[right].lower():
                return is_palindrome(left+1,right) or is_palindrome(left,right-1)
            
            left+=1
            right-=1

        return True

        