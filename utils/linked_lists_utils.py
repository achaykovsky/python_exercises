from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: List[int]) -> ListNode:
    if not arr:  # If the list is empty, return None
        return None

    head = ListNode(arr[0])  # Initialize the head of the linked list
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)  # Create a new node and link it
        current = current.next  # Move to the next node

    return head


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val)
        current = current.next
