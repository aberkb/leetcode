#Given a positive integer num consisting only of digits 6 and 9.

#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
#brute force
class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = list(str(num))
        idx = 0
        for i, letter in enumerate(str_num):
            if letter  == "6":
                idx = i
                break
        str_num[idx] = "9"
        return int("".join(str_num))

#Runtime: 44 ms, faster than 20.37% of Python3 online submissions for Maximum 69 Number.
#Memory Usage: 13.9 MB, less than 21.28% of Python3 online submissions for Maximum 69 Number.

#dynamic
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        num_dict = {i:v for i, v in enumerate(num_list)}
        for i, v in num_dict.items():
            if v == "6":
                num_dict[i] = "9"
                break
        return "".join(num_dict.values())
#Runtime: 32 ms, faster than 59.70% of Python3 online submissions for Maximum 69 Number.
#Memory Usage: 14 MB, less than 5.67% of Python3 online submissions for Maximum 69 Number.
