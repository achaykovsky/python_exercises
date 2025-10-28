from typing import List


# Optimal solution for the Gas Station problem using a greedy approach.

# Time Complexity: O(n)
# Space Complexity: O(1)
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # if the total gas is less than the total cost completing the circuit is impossible
    if sum(gas) < sum(cost):
        return -1

    start_index, tank = 0, 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # If current gas is negative, reset the start index because we cannot start before this point
        if tank < 0:
            start_index, tank = i + 1, 0
    return start_index


if __name__ == '__main__':
    gas, cost = [2, 5, 1, 3], [3, 2, 1, 4]
    result = canCompleteCircuit(gas, cost)
    print(result)
