# This is a generic file for the trivial solution

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# The idea is not to reverse the values!
# The idea is to change the DIRECTION of the pointing!

# Time: O(n) Space: O(1)
def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head

    # 1->2->3->4->5->None
    # 5->4->3->2->1->None

    while current:
        next_node = current.next  # saving the pointer for future use
        current.next = prev
        prev = current
        current = next_node

    return prev  # after the reversing the list, the new head is going to be in the prev


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print("Original linked list:")
    print_linked_list(head)

    reversed_head = reverse_linked_list(head)
    print("\nReversed linked list:")
    print_linked_list(reversed_head)
