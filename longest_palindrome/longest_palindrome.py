class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = 0

        for ch in set(s):
            a = s.count(ch)
            if a % 2 == 0:
                n += a
            else:
                n += a - 1

        if n < len(s):
            n += 1

        return n