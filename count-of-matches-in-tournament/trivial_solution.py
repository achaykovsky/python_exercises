# This is a generic file for the trivial solution

def numberOfMatches(matches: int) -> int:
    result = 0
    teams = matches
    while teams > 1:
        if teams % 2 == 0:
            matches = teams // 2
        else:
            matches = ((teams - 1) // 2)
        teams = teams - matches
        result += matches
    return result


if __name__ == '__main__':
    n = 7
    result = numberOfMatches(n)
    print(result)
