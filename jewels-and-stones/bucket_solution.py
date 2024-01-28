# This is a generic file for the trivial solution

def numJewelsInStones(jewels, stones):
    existing_small_jewels = [0] * 26
    existing_small_stones = [0] * 26
    existing_big_jewels = [0] * 26
    existing_big_stones = [0] * 26
    result = 0
    for jewel in jewels:
        if jewel.islower():
            existing_small_jewels[ord(jewel) - ord('a')] += 1
        else:
            existing_big_jewels[ord(jewel) - ord('A')] += 1

    for stone in stones:
        if stone.islower():
            existing_small_stones[ord(stone) - ord('a')] += 1
        else:
            existing_big_stones[ord(stone) - ord('A')] += 1

    for i, existing_jewel in enumerate(existing_small_jewels):
        if existing_jewel > 0:
            result += existing_small_stones[i]
    for i, existing_jewel in enumerate(existing_big_jewels):
        if existing_jewel > 0:
            result += existing_big_stones[i]

    return result


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    result = numJewelsInStones(jewels, stones)
    print(result)
