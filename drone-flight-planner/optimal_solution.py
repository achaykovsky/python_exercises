from typing import List


# Since the units are going up and down through the first height the will cancel each other,
# so the difference between the max and the first height will be the answer of the energy needed
def drone_flight_planner(route: List[List[int]]) -> int:
    route = [z for _, _, z in route]
    first_height = route[0]
    max_height = max(route)
    return max_height - first_height


if __name__ == '__main__':
    route = [[0, 2, 10], [3, 5, 0], [9, 20, 6], [10, 12, 15], [10, 10, 8]]
    result = drone_flight_planner(route)
    print(result)
