from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list_from_array(arr: List[int]) -> ListNode:
    if not arr:  # If the list is empty, return None
        return None

    head = ListNode(arr[0])  # Initialize the head of the linked list
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)  # Create a new node and link it
        current = current.next  # Move to the next node

    return head


def print_linked_list(head: ListNode) -> None:
    output = ["head"]
    current = head
    while current:
        output.append(str(current.val))
        current = current.next
    output.append("null")
    print(" -> ".join(output))


def create_linked_list_with_cycle(arr: [int], pos: int) -> ListNode:
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


def append_linked_lists(head1: ListNode, head2: ListNode):
    current = head1
    while current.next:
        current = current.next
    current.next = head2
