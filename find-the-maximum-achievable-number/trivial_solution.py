# This is a generic file for the trivial solution

def theMaximumAchievableX(num: int, t: int) -> int:
    num += t * 2
    return num


if __name__ == '__main__':
    num, t = 4, 1
    result = theMaximumAchievableX(num, t)
    print(result)
