import math
from typing import List


# k = bananas per hour that Koko can eat
# h = upper bound of the hours Koko has to finish all the bananas
# We want to know if Koko can finish all the bananas with speed k in h hours

# The idea is that we are looking for the minimal number of bananas that Koko should eat per hour,
# in order to finish all the piles in h hours


# Time Complexity: O(n*max(piles))
# Space Complexity: O(1)

def minEatingSpeed(piles: List[int], h: int) -> int:
    max_bananas_in_pile = max(piles)
    for candidate in range(1, max_bananas_in_pile):  # O(max(piles))
        result = 0
        for pile in piles:  # O(n)
            current_koko_speed = math.ceil(pile / candidate)
            result += current_koko_speed
        if result <= h:
            return candidate
    return -1


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    result = minEatingSpeed(piles, h)
    print(result)
