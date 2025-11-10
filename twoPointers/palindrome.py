# Test if string s is a palindrome
# First implementation: reverse string and boolean compare to return True or False
def isPalindrome(self, s: str) -> bool:
        newString = ''
        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]
# Second implementation: two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            # skip non alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            # and here
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True