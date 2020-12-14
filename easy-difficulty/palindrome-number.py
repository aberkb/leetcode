#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
#Follow up: Could you solve it without converting the integer to a string?
#
#Example 1:
#
#Input: x = 121
#Output: true

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == (str(x))[::-1]:
            return True
        return False

#Runtime: 56 ms, faster than 78.91% of Python3 online submissions for Palindrome Number.
#Memory Usage: 14.2 MB, less than 58.65% of Python3 online submissions for Palindrome Number.

#without converting to str

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = []
        if x<0:
            return 0
        while x:
            num += [x % 10]
            x //= 10

        return num == num[::-1]
