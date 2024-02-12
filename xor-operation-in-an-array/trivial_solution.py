# This is a generic file for the trivial solution

def solution(n: int, start: int) -> int:
    nums = list(map(lambda i: start + 2 * i, range(n)))
    result = nums[0]
    for i in range(len(nums)):
        result = nums[i] ^ result
    return result


if __name__ == '__main__':
    n = 5
    start = 0
    result = solution(n, start)
    print(result)
