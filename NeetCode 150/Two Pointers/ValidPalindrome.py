class Solution:
    def isPalindrome(self, s: str) -> bool:
        """

        Simple solution

        new_string = ""
        for c in s:
            if c.isalnum():
                new_string+= c.lower()
        return new_string == new_string[::-1]
        
        """
        
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
        return True

        