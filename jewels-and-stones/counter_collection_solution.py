from collections import Counter


def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """

    c = Counter(stones)

    return sum(c[j] for j in jewels)


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    result = numJewelsInStones(jewels, stones)
    print(result)
