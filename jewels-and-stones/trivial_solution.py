# This is a generic file for the trivial solution

def numJewelsInStones(jewels, stones):
    result = 0
    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                result += 1
    return result


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    result = numJewelsInStones(jewels, stones)
    print(result)
