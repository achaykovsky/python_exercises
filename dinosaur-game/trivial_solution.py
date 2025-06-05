from typing import List


# Time Complexity: O(m) where m is the maximum obstacle
# Space Complexity: O(m)
def canSurvive(obstacles: List[int], jump_distance: int) -> bool:
    obstacle_set = set(obstacles)
    max_obstacle = max(obstacles) if obstacles else 0
    pos = 0
    max_reach = 0

    while pos <= max_reach:
        if pos not in obstacle_set:
            for step in range(1, jump_distance + 1):  # Check all possible jumps
                next_pos = pos + step
                if next_pos not in obstacle_set:
                    max_reach = max(max_reach, next_pos)  # update the maximum reachable position

        if max_reach > max_obstacle:  # if we can jump over the last obstacle
            return True

        pos += 1

    return False


if __name__ == '__main__':
    obstacles = []
    jump_distance = 2
    result = canSurvive(obstacles, jump_distance)
    print(result)
