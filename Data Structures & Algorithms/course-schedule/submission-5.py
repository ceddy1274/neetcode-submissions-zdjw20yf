class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course in prerequisites:
            preMap[course[0]].append(course[1])
        
        visitSet = set()
        def dfs(currCourse):
            if currCourse in visitSet:
                return False
            if preMap[currCourse] == []:
                return True

            visitSet.add(currCourse)
            for course in preMap[currCourse]:
                if not dfs(course):
                    return False
            visitSet.remove(currCourse)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True