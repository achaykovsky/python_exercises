from collections import defaultdict
from typing import List


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# V = numCourses, E = number of prerequisites


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    result = []
    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(course: int) -> bool:
        # revisiting a node still in recursion stack -> cycle detected
        if visited[course] == 1:
            return False

        # finished processing all the prerequisites
        if visited[course] == 2:
            return True

        visited[course] = 1  # mark as visiting
        for neighbor in graph[course]:
            # Looking for a cycle when traversing through the neighbors
            # Neighbor has a cycle -> propagate failure
            if not dfs(neighbor):
                return False

        # No Cycle Detected -> the course is fully processed
        visited[course] = 2
        result.append(course)
        return True

    # Traverse all the courses (some may be disconnected components!)
    for course in range(numCourses):
        if visited[course] == 0:
            if not dfs(course):
                return []  # cycle detected -> no topological order

    return result[::-1]  # post-order traversal gives us the list of prerequisites in reverse
