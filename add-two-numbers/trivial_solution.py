from typing import Optional

from utils.linked_lists_utils import ListNode, create_linked_list, print_linked_list


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    cur = result
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        curr_digit = val1 + val2 + carry
        carry = curr_digit // 10
        curr_digit = curr_digit % 10
        cur.next = ListNode(curr_digit)

        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return result.next


if __name__ == '__main__':
    l1 = [7]
    l2 = [8]

    head1 = create_linked_list(l1)
    head2 = create_linked_list(l2)

    result = addTwoNumbers(head1, head2)
    print_linked_list(result)
