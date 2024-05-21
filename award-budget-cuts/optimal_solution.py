from typing import List


def find_grants_cap(grants_array: List[int], new_budget: int) -> int:
    grants_array.sort()
    students = len(grants_array)
    for i in range(len(grants_array)):
        grant_money = grants_array[i] * students
        if grant_money >= new_budget:
            cap = float(new_budget / students)
            return cap
        students -= 1
        new_budget -= grants_array[i]


if __name__ == '__main__':
    grants_array = [21, 100, 50, 120, 130, 110]
    new_budget = 140
    result = find_grants_cap(grants_array, new_budget)
    print(result)
