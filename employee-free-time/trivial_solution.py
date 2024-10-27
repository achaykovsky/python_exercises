# This is a generic file for the trivial solution
from collections import defaultdict
from typing import List


def employee_free_time(schedule: List[List[list[int]]]) -> List[List[int]]:
    result = []
    if not schedule:
        return result

    # Flatten the list of lists into a single list of intervals to find all the busy times
    intervals = [interval for sublist in schedule for interval in sublist]

    intervals.sort(key=lambda x: x[0])  # sorting by the beginning

    merged = [intervals[0]]

    for interval in intervals[1:]:

        if interval[0] <= merged[-1][1]:

            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        else:

            merged.append(interval)

    size_of_merge_time = len(merged)
    for i, interval in enumerate(merged, start=1):  # going through the intervals to find free time
        if i < size_of_merge_time:
            result.append([merged[i - 1][1], merged[i][0]])  # returning the max of the start and the min of the ending

    return result


if __name__ == '__main__':
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]], [[12, 15]]]
    result = employee_free_time(schedule)
    print(result)
