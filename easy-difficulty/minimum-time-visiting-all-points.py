class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans =0
        for i in range(len(points)-1):
            origin = points[i]
            destination = points[i+1]
            x = destination[0] - origin[0]
            y = destination[1] - origin[1]
            if abs(x) > abs(y):
                ans = ans + abs(x)
            elif abs(y) > abs(x):
                ans = ans + abs(y)
            else:
                ans = ans + abs(x)
        return ans
