from collections import Counter


# Time Complexity: O(n)
# Space Complexity: O(n)
def maximize_number(num: str) -> str:
    num_list = list(str(num))
    last_indices_mapping = {int(x): idx for idx, x in
                            enumerate(num_list)}  # each digit and its last_indices_mapping index

    for i, x in enumerate(num_list):  # O(n)
        for digit in range(9, int(x), -1):  # O(10) which is constant
            if digit in last_indices_mapping and last_indices_mapping[digit] > i:
                num_list[i], num_list[last_indices_mapping[digit]] = num_list[last_indices_mapping[digit]], num_list[i]
                return ''.join(num_list)
    return num


if __name__ == '__main__':
    res = maximize_number("45929")  # 95924
    # res = maximize_number("2999")  # 9992
    # res = maximize_number("978")  # 987
    # res = maximize_number("9856")  # 9865
    print(res)
