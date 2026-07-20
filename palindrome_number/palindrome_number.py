class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


solution = Solution()

number = 121

if solution.isPalindrome(number):
    print("this is a palindrome")
else:
    print("this is not a palindrome")