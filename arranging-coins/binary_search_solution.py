# Arithmetic explanation of how we calculate the number of the coins

# coins_sum = Sn = ([2*a1 + d(n-1)]*n)//2 ===>
# a1 = 1 ===>
# Sn = (n*(n+1))//2 ===>
# n/2 * (n+1)
# where n is the largest number such as the coins_sum<=n given in the question
# Note: Those are totally 2 different n!!

# Time Complexity: O(logn) - where n is the total number of the coins
# Space Complexity: O(1)
def arrangeCoins(n: int) -> int:
    l, r = 1, n
    result = 0

    while l <= r:
        mid = (l + r) // 2
        coins_sum = (mid * (mid + 1)) // 2  # arithmetic series formula

        if coins_sum > n:
            r = mid - 1
        else:
            l = mid + 1
            result = max(mid, result)

    return result


if __name__ == '__main__':
    n = 5
    result = arrangeCoins(n)
    print(result)
