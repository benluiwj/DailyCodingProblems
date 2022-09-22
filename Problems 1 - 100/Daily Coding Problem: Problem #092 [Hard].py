# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# We're given a hashmap associating each courseId key with a list of courseIds 
# values, which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.

# Return null if there is no such ordering.

# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'],
# 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
from typing import *

"""
actually a dfs question about topo sorting. reverse the mapping order to obtain a map that contains prerequisites -> course and not course -> prereq

when we visit the course, can just add into the schedule.

to see if its possible check the resulting length of the scheduel in the end.


"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [i for i in range(numCourses)]
        completed = set()
        postreq_map = dict()
        prereq_map = dict()
        ordering = []
        
        for a, b in prerequisites:
            if a in prereq_map:
                prereq_map[a].add(b)
            
            else:
                prereq_map[a] = {b}
            
            if b in postreq_map:
                postreq_map[b].add(a)
            
            else:
                postreq_map[b] = {a}
        
        def helper(curr):
            last = curr[-1]
            if last not in postreq_map:
                return
            
            for course in postreq_map[last]:
                if course not in completed:
                    prereq_map[course].remove(last)
                    if not prereq_map[course]:
                        completed.add(course)
                        ordering.append(course)
                        curr.append(course)
                        helper(curr)
                        curr.pop()
            
        
        for course in courses:
            if course not in prereq_map:
                completed.add(course)
                ordering.append(course)
                helper([course])
        
        print(ordering)

        if len(ordering) == numCourses:
            return ordering
        

sol = Solution()
# sol.findOrder(2, [[1,0]])
sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])