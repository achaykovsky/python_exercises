from typing import List
from collections import defaultdict


# Time Complexity: O(n^2)
# Space Complexity: O(n)
def find_busiest_period(data: List[List[int]]) -> int:
    people_counts = defaultdict(list)
    sum_result, max_result, timestamp_result = 0, 0, 0

    for element in data:
        people_num = element[1]
        if element[2] == 0:  # when people leave, we count them negatively
            people_num *= -1
        people_counts[element[0]].append(people_num)

    for key, people_count in people_counts.items():
        temp_sum = sum(people_count)  # O(n) WC
        sum_result += temp_sum
        if sum_result > max_result:
            max_result = sum_result
            timestamp_result = key

    return timestamp_result


if __name__ == '__main__':
    data = [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1],
            [1487801478, 18, 0], [1487801478, 18, 1], [1487901013, 1, 0], [1487901211, 7, 1],
            [1487901211, 7, 0]]
    result = find_busiest_period(data)
    print(result)
