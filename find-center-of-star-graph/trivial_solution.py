from typing import List


def solution(edges: List[List[int]]) -> int:
    edges_number = len(edges)
    freq_array = [0] * (edges_number + 2)
    for edge in edges:
        # the inner loop always two, so the complexity will be 2n-> O(n)
        for i in edge:
            freq_array[i] += 1

    for i, num in enumerate(freq_array):
        if num == edges_number:
            return i


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    result = solution(edges)
    print(result)
