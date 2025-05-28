# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        curr = head
        while curr : 
            q.append(curr)
            curr = curr.next

        curr = q.popleft()
        toggle = True 
        while q : 
            if toggle : 
                curr.next = q.pop()
            else : 
                curr.next = q.popleft()
            curr = curr.next 
            toggle = not toggle
        curr.next = None


