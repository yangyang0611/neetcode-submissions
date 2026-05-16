class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        reverse = string[::-1]

        return string == reverse