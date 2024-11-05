# This is a generic file for the trivial solution
import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,
                       num * (-1))  # inserting into the max heap (inserted negative numbers of the original)

        # making sure that every num in the max_heap <= every num in the min_heap
        if self.min_heap and self.max_heap and (
                (-1) * self.max_heap[0] > self.min_heap[0]):  # the max element is bigger than the min element
            value = (-1) * heapq.heappop(
                self.max_heap)  # pop the last value from the max heap to insert into the min_heap
            heapq.heappush(self.min_heap, value)  # insert

        # validate the size are equal
        if len(self.max_heap) > len(self.min_heap) + 1:  # the max heap is bigger than the min_heap
            value = (-1) * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)  # move the value from the max_heap to the min_heap
        if len(self.min_heap) > len(self.max_heap) + 1:  # the min_heap is bigger than the max_heap
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-1) * value)  # move the value from the min_heap to the max_heap

    def findMedian(self) -> float:
        # for example (2,3,5) and (4,7) : median = 5
        if len(self.max_heap) > len(self.min_heap):  # there are more elements on the max heap. The median is the max
            return (-1) * self.max_heap[0]
            # for example (2,3) and (4,5,7) : median = 4
        elif len(self.max_heap) < len(self.min_heap):  # there are more elements on the min heap. The median is the min
            return self.min_heap[0]
        else:
            # for example (2,3) and (4,7) : median = 3.5
            return ((-1) * self.max_heap[0] + self.min_heap[
                0]) / 2  # the number of the elements is equal. The median is average of the two middles


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    # medianFinder.addNum(2)  # arr = [1, 2]
    medianFinder.findMedian()  # return 1.5(i.e., (1 + 2) / 2)
    # medianFinder.addNum(3)  # arr[1, 2, 3]
    # medianFinder.findMedian()  # return 2.0
