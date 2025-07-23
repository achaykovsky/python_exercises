import heapq


# Median is the middle value in a sorted list of numbers.
# If the list has an even number of elements, the median is the average of the two middle values.


# This solution uses two heaps:
# - A max heap to store the lower half of the numbers (inverted to use Python's min-heap as a max-heap).
# - A min heap to store the upper half of the numbers.


# Time Complexity: O(log n) for addNum, O(1) for findMedian
# Space Complexity: O(n) for storing the numbers in heaps
class MedianFinder:

    def __init__(self):
        self.right_half_min_heap, self.left_half_max_heap = [], []

    # Time Complexity: O(log n)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_half_max_heap,
                       num * (-1))  # inserting into the max heap (inserted negative numbers of the original)

        # making sure that every num in the left_half_max_heap <= every num in the right_half_min_heap
        if self.right_half_min_heap and self.left_half_max_heap and (
                (-1) * self.left_half_max_heap[0] > self.right_half_min_heap[
            0]):  # the max element is bigger than the min element

            value = (-1) * heapq.heappop(
                self.left_half_max_heap)  # pop the last value from the max heap to insert into the right_half_min_heap
            heapq.heappush(self.right_half_min_heap, value)  # insert

        # validate the size are equal
        if len(self.left_half_max_heap) > len(
                self.right_half_min_heap) + 1:  # the max heap is bigger than the right_half_min_heap

            value = (-1) * heapq.heappop(self.left_half_max_heap)
            heapq.heappush(self.right_half_min_heap,
                           value)  # move the value from the left_half_max_heap to the right_half_min_heap

        if len(self.right_half_min_heap) > len(
                self.left_half_max_heap) + 1:  # the right_half_min_heap is bigger than the left_half_max_heap

            value = heapq.heappop(self.right_half_min_heap)
            heapq.heappush(self.left_half_max_heap,
                           (-1) * value)  # move the value from the right_half_min_heap to the left_half_max_heap

    # Time Complexity: O(1)
    def findMedian(self) -> float:
        # for example (2,3,5) and (4,7) : median = 5
        if len(self.left_half_max_heap) > len(
                self.right_half_min_heap):  # there are more elements on the max heap. The median is the max
            return (-1) * self.left_half_max_heap[0]

            # for example (2,3) and (4,5,7) : median = 4
        elif len(self.left_half_max_heap) < len(
                self.right_half_min_heap):  # there are more elements on the min heap. The median is the min
            return self.right_half_min_heap[0]

        else:
            # for example (2,3) and (4,7) : median = 3.5
            return ((-1) * self.left_half_max_heap[0] + self.right_half_min_heap[
                0]) / 2  # the number of the elements is equal. The median is average of the two middles


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    print(medianFinder.findMedian())  # (1 + 2) / 2 = 1.5
    # medianFinder.addNum(3)  # arr[1, 2, 3]
    # medianFinder.findMedian()  # return 2.0
