from typing import Optional

from utils.linked_lists_utils import ListNode, create_linked_list_from_array, print_linked_list


# Time Complexity: O(max(m,n))
# Space Complexity: O(max(m,n))
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    cur = result
    carry = 0

    while l1 or l2 or carry:
        # Validate that l1/l2 is not None because we might have different lengths
        # If one of them is None, we consider its value as 0
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        curr_digit = val1 + val2 + carry
        carry = curr_digit // 10
        curr_digit = curr_digit % 10
        cur.next = ListNode(curr_digit)

        # Move to the next nodes
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return result.next


if __name__ == '__main__':
    l1 = [7]
    l2 = [8]

    head1 = create_linked_list_from_array(l1)
    head2 = create_linked_list_from_array(l2)

    result = addTwoNumbers(head1, head2)
    print_linked_list(result)
