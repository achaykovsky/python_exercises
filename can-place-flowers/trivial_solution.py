from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    possible_flowers = 0
    padded_flowerbed = [0] + flowerbed + [0]

    for i in range(1, len(padded_flowerbed) - 1):  # ignoring first and last
        if padded_flowerbed[i - 1] == 0 and padded_flowerbed[i] == 0 and padded_flowerbed[i + 1] == 0:
            possible_flowers += 1
            padded_flowerbed[i] = 1

    return n <= possible_flowers  # might be more possible places that we need


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 0, 0, 1]
    n = 2
    result = canPlaceFlowers(flowerbed, n)
    print(result)
