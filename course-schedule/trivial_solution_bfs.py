from collections import deque, defaultdict
from typing import List


# Kahn's Algorithm for Course Schedule
# The idea is to use a queue to keep track of courses that can be taken (i.e., courses with no prerequisites).
# We build a directed graph where each course points to the courses that depend on it (i.e., the courses that have it as a prerequisite).

# Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
# Space Complexity: O(V + E) for storing the graph and in-degrees
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)

    if not prerequisites:
        return True

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

    enrolled_courses = 0
    while queue:
        course = queue.popleft()
        # Enroll in the course
        enrolled_courses += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1

            # all prerequisites for next_course are satisfied (in_degree becomes 0)
            if in_degree[next_course] == 0:
                queue.append(next_course)
    return enrolled_courses == numCourses


if __name__ == '__main__':
    num_courses = 2
    prerequisites = [[1, 0]]
    result = canFinish(num_courses, prerequisites)
    print(result)
