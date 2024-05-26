# This is a generic file for the trivial solution
import heapq
from typing import List


def solution(solution_input):
    result = []
    return result


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap, val)


if __name__ == '__main__':
    # Your KthLargest object will be instantiated and called as such:

    nums = [4, 5, 8, 2]
    obj = KthLargest(3, nums)
    param_1 = obj.add(val=5)
