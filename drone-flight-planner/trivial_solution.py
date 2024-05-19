from typing import List


def drone_flight_planner(route: List[List[int]]) -> int:
    route = [z for _, _, z in route]
    diffs = 0
    l = 0
    for r in range(len(route)):
        if (route[r] > route[l]):
            diffs += (route[r] - route[l])  # adding to the sum all the differnces above the first entry
            l = r  # setting the new max
    return diffs


if __name__ == '__main__':
    route = [[0, 2, 10], [3, 5, 0], [9, 20, 6], [10, 12, 15], [10, 10, 8]]

    result = drone_flight_planner(route)
    print(result)
