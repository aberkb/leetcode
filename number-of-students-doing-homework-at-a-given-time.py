#Given two integer arrays startTime and endTime and given an integer queryTime.

#The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

#Return the number of students doing their homework at time queryTime.
#More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for low, high in zip(startTime, endTime):
            if low <= queryTime <= high:
                ans += 1
        return ans

#Runtime: 32 ms, faster than 93.71% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 14 MB, less than 8.91% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
