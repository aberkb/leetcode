#check the question here : https://leetcode.com/problems/roman-to-integer/
#Example 1:

#Input: s = "III"
#Output: 3

#Example 2:

#Input: s = "IV"
#Output: 4

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
		    "C": 100,
		    "D": 500,
		    "M": 1000,
        }
        result = 0

        for i in range(len(s)):
            current_value = roman_to_int_dict.get(s[i])
            if i+1 < len(s) and roman_to_int_dict.get(s[i+1]) > current_value:
                result -= current_value
            else:
                result += current_value
                
        return result
