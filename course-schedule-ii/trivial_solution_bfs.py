from typing import List
from collections import deque, defaultdict


# Kahn's Algorithm for Course Schedule (Topological Sort - Searching by BFS)

# A Topological Sort of a directed graph is a linear ordering of its vertices such that:
# For every directed edge u -> v, vertex u comes before vertex v in the ordering.

# The Algorithm
# The idea is to use a queue to keep track of courses that can be taken (i.e., courses with no prerequisites).
# We build a directed graph where each course points to the courses that depend on it (i.e., the courses that have it as a prerequisite).

# Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
# Space Complexity: O(V + E) for storing the graph and in-degrees
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    result = []

    graph = defaultdict(list)

    in_degree = [0] * numCourses

    # Build the graph and calculate in-degrees
    # prerequisites are in the form [course, prerequisite]
    for course, prerequisite in prerequisites:
        in_degree[course] += 1
        graph[prerequisite].append(course)

    queue = deque()
    # Initialize the queue - add all courses with no prerequisites to the queue
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()
        # Enroll in the course
        result.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1

            # all prerequisites for next_course are satisfied (in_degree becomes 0)
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # Some courses were never processed ->  in-degree never dropped to 0 -> Cycle detected
    if len(result) != numCourses:
        result = []

    return result


if __name__ == '__main__':
    num_courses = 2
    prerequisites = [[1, 0]]
    result = findOrder(num_courses, prerequisites)
    print(result)
