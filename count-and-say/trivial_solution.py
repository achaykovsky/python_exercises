# Recursive solution for the "Count and Say" problem

# Time Complexity: O(n * 2^m) where m is the length of the string at step n
# Space Complexity: O(2^m) where m is the length of the string at step
def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    prev_counter = countAndSay(n - 1)
    return rle(prev_counter)


# Time Complexity: O(m) where m is the length of the string
# Space Complexity: O(m) where m is the length of the string
def rle(s: str) -> str:
    res = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # same group
            count += 1
        else:
            res.append(str(count))  # append count of previous group
            res.append(s[i - 1])  # append character of previous group
            count = 1

    # append the last group
    res.append(str(count))
    res.append(s[-1])

    return "".join(res)


if __name__ == '__main__':
    n = 4
    result = countAndSay(n)
    print(result)
