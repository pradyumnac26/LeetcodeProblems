# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # If the list is empty or has only one node
            return head

        # Initialize pointers
        odd = head  # Points to the first odd-indexed node
        even = head.next  # Points to the first even-indexed node
        even_head = even  # Save the head of the even list to connect later

        # Reorder the nodes
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next       # Move the odd pointer forward

            even.next = odd.next  # Link the next even node
            even = even.next      # Move the even pointer forward

        # Connect the end of the odd list to the head of the even list
        odd.next = even_head

        return head
