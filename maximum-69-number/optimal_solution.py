# Problem: https://leetcode.com/problems/maximum-69-number/

# Time Complexity: O(d)
# Space Complexity: O(d)
def maximum69Number(num: int) -> int:
    num_str = list(str(num))
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str[i] = '9'
            break
    return int(''.join(num_str))


if __name__ == '__main__':
    num = 9669
    result = maximum69Number(num)
    print(result)
