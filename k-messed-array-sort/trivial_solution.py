import heapq


def sort_k_messed_array(arr, k):
    heap = arr[:k + 1]  # k+1 because we would like to have k more elements, and the upper bound is not included
    heapq.heapify(heap)
    result = []

    for num in arr[k + 1:]:
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, num)

    while heap:  # popping out the elements left
        result.append(heapq.heappop(heap))

    return result


if __name__ == '__main__':
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    result = sort_k_messed_array(arr, k)
    print(result)
