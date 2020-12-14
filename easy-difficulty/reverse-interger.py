#Given a 32-bit signed integer, reverse digits of an integer.
#
#Note:
#Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

#Example 1:
#
#Input: x = 123
#Output: 321

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = int("-" + str(x).replace("-","")[::-1])
        else:
            result = int(str(x)[::-1])
        if result > pow(-2,31) and result < pow(2, 31):
            return result
        else:
            return 0

#Runtime: 32 ms, faster than 62.40% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.4 MB, less than 21.24% of Python3 online submissions for Reverse Integer.
