# Problem: https://leetcode.com/problems/maximum-69-number/

# Time Complexity: O(d^2) - since we are creating a new string in each iteration
# Space Complexity: O(d)
def maximum69Number(num: int) -> int:
    num_str = str(num)
    new_num = ""
    updated = False
    for digit in num_str:
        # we will enter here only once when updated is False and change it to True
        if digit == '6' and not updated:
            new_num += '9'  # makes a new string, so complexity is O(d)
            updated = True
        else:
            new_num += digit

    return int(new_num)


if __name__ == '__main__':
    num = 9669
    result = maximum69Number(num)
    print(result)
