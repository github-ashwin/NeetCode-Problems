def isPalindromeAfterDeleteFirst(s):
    left, right = 1, len(s) - 1  # start from index 1, since first char is skipped
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
print(isPalindromeAfterDeleteFirst("radar"))  # True -> "adar"
print(isPalindromeAfterDeleteFirst("abca"))   # False -> "bca"
print(isPalindromeAfterDeleteFirst("hello"))  # False
