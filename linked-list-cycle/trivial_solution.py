# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:  # fast will reach the end faster, so we should validate it's existence and the next for it
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # after advancing both of them we validate if there are on the same position
            return True

    return False


def create_linked_list(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head


if __name__ == '__main__':
    head = create_linked_list([3, 2, 0, -4], 1)
    # head = create_linked_list([1, 2], 0)
    # head = create_linked_list([1], -1)

    result = hasCycle(head)
    print(result)
