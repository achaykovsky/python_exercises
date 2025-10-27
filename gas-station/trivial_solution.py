from typing import List


# Brute force solution for the Gas Station problem.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)

    # If the total gas is less than the total cost, completing the circuit is impossible
    if sum(gas) < sum(cost):
        return -1

    # Try starting from each gas station
    # and check if we can complete the circuit

    for start in range(n):
        tank = 0
        completed = True

        for i in range(n):
            # Calculate the index in a circular manner
            # (start + i) % n ensures we wrap around the array

            idx = (start + i) % n
            tank += gas[idx] - cost[idx]

            # If at any point the tank goes negative, we cannot complete the circuit
            if tank < 0:
                completed = False
                break

        if completed:
            return start

    return -1


if __name__ == '__main__':
    gas, cost = [2, 5, 1, 3], [3, 2, 1, 4]
    result = canCompleteCircuit(gas, cost)
    print(result)
