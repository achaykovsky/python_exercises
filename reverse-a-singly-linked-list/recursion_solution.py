# This is a generic file for the trivial solution

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# The idea is not to reverse the values!
# The idea is to change the DIRECTION of the pointing!

# Time: O(n) Space: O(n)
def reverse_linked_list(head: ListNode) -> ListNode:
    if not head:
        return None

    new_head = head

    if head.next:
        new_head = reverse_linked_list(head.next)
        head.next.next = head
    head.next = None

    return new_head


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    print("Original linked list:")
    print_linked_list(head)

    reversed_head = reverse_linked_list(head)
    print("\nReversed linked list:")
    print_linked_list(reversed_head)
