# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


def find_busiest_period(data: List[List[int]]) -> int:
    max_result, sum_result, timestamp_result = 0, 0, 0

    for i in range(len(data)):
        if data[i][2] == 0:  # summing all the people according entrance/exit
            sum_result -= data[i][1]  # exit
        else:
            sum_result += data[i][1]  # entrance

        if i < len(data) - 1 and data[i][0] == data[i + 1][0]:  # the time is equal
            continue  # no need to validate the max until we finish summarizing all the people

        if sum_result > max_result:  # finding the max sum and it's timestamp
            max_result = sum_result
            timestamp_result = data[i][0]

    return timestamp_result


if __name__ == '__main__':
    data = [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1],
            [1487801478, 18, 0], [1487801478, 18, 1], [1487901013, 1, 0], [1487901211, 7, 1],
            [1487901211, 7, 0]]
    result = find_busiest_period(data)
    print(result)
