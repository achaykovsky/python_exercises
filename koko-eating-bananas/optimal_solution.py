import math
from typing import List


# k = bananas per hour that Koko can eat
# h = upper bound of the hours Koko has to finish all the bananas
# We want to know if Koko can finish all the bananas with speed k in h hours
def can_koko_eat_all_bananas(piles: List[int], k: int, h: int) -> bool:
    total_hours = 0
    for pile in piles:
        # Calculate how much hours it takes to eat k bananas per hour
        hours_eat_pile_at_speed_k = math.ceil(pile / k)
        # add the hours for that pile to the total number of the hours
        total_hours += hours_eat_pile_at_speed_k
    # Koko will be able to finish all the bananas in h hours
    return total_hours <= h


# The idea is that we are looking for the minimal number of bananas that Koko should eat per hour,
# in order to finish all the piles in h hours


# Time Complexity: O(n*log(max(piles)))
# Space Complexity: O(1)

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_koko_eat_all_bananas(piles, mid, h):
            # Koko was able to eat the bananas in h hours -> look into the left side to find a smaller threshold
            right = mid
        else:
            # Koko wasn't able to eat the bananas in h hours -> look for a bigger k (bananas-per-hour) to finish all of them
            left = mid + 1
    # We asked for the minimum of piles
    return left


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    result = minEatingSpeed(piles, h)
    print(result)
