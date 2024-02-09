# This is a generic file for the trivial solution
from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    wealth = []
    for account in accounts:
        wealth.append(sum(account))
    result = max(wealth)
    return result


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    result = maximumWealth(accounts)
    print(result)
