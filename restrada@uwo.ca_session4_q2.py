
# given array of enteringEdges, 0 to numCourses-1
# from prereqs[i] = [ai,bi], find if you can take all enteringEdges

from typing import List
from collections import deque

'''
SOLUTION
- if we have courses open and no prerequisites, return True
- fill graph with vertices paths and track how many entering edges for each vertex has
- queue all possible starting positions (vertices with no entering edges) and search thru each
- implement dfs to track how many edges remain at each neighbor nodes
- when no edges remain, that class is added to the count
- when the final node is reached, if there is more counted classes than numCourses available, return False
'''

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if numCourses and len(prerequisites) == 0: # O(1)
            return True

        graph = [[] for _ in range(numCourses)] # O(V) to populate empty graph

        enteringEdges = [0] * numCourses # O(1)

        for course, prereq in prerequisites: # O(E)
            graph[prereq].append(course)
            enteringEdges[course] += 1
        
        q = deque()

        for x in range(0, len(enteringEdges)):  # O(E)
            if enteringEdges[x] == 0:
                q.append(x)

        count = 0

        while len(q):   # O(V) worst case
            curr = q.popleft()  #O(1)

            if enteringEdges[curr] == 0:
                count += 1
            
            for neighbor in graph[curr]:    # O(V) worst case
                enteringEdges[neighbor] -= 1
                if enteringEdges[neighbor] == 0:
                    q.append(neighbor)
            
        return True if count == numCourses else False

# Given Test
numCourses = 5
prerequisites = [[1,0],[4,1],[4,2],[3,1],[5,4],[5,3]]

sol = Solution()
print(sol.canFinish(numCourses, prerequisites))

'''
Time Complexity: O(V + E) as we need to go through every vertex and check every edge
Space Complexity: O(V) worst case as we store the graph with every vertex 
'''