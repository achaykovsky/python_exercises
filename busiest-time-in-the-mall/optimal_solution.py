from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def find_busiest_period(data: List[List[int]]) -> int:
    max_result = 0
    sum_result, timestamp_result = 0, 0
    i, j, k = 0, 0, 0  # can be replaced by one variable and initialized after each loop
    first_id = 0

    while i < len(data):  # marking as negative all the numbers for people who left
        if data[i][2] == 0:  # when people left
            data[i][1] *= -1
        i += 1

    while j + 1 < len(
            data):  # summing into the first array the total sum of the same moment (making the sum for current time unique)
        if data[j][0] == data[j + 1][0]:
            data[first_id][1] += data[j + 1][1]
            data[j + 1][1] = 0  # initializing every list that we already summed up
        else:
            first_id = j + 1  # first element of the time (and the only if it's unique)
        j += 1

    while k < len(data):  # summing all the people and looking for the max, marking the timestamp
        sum_result += data[k][1]
        if max_result < sum_result:
            max_result = sum_result
            timestamp_result = data[k][0]
        k += 1

    return timestamp_result


if __name__ == '__main__':
    data = [[1487799425, 14, 1], [1487799425, 4, 0], [1487799425, 2, 0], [1487800378, 10, 1],
            [1487801478, 18, 0], [1487801478, 18, 1], [1487901013, 1, 0], [1487901211, 7, 1],
            [1487901211, 7, 0]]
    result = find_busiest_period(data)
    print(result)
