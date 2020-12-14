#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
#Return the destination city, that is, the city without any path outgoing to another city.

#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = []
        for couples in paths:
            origins.append(couples[0])

        for couples in paths:
            if not couples[1] in origins:
                return couples[1]

#Runtime: 84 ms, faster than 21.40% of Python3 online submissions for Destination City.
#Memory Usage: 13.8 MB, less than 58.79% of Python3 online submissions for Destination City.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_dict = dict(paths)
        initial = paths[0][0]
        while(True):
            if path_dict.get(initial):
                initial = path_dict[initial]
            else:
                return initial

#Runtime: 124 ms, faster than 5.91% of Python3 online submissions for Destination City.
#Memory Usage: 13.8 MB, less than 71.36% of Python3 online submissions for Destination City.
