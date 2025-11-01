
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr:
            if curr.val in s:
                prev.next = curr.next  
            else:
                prev = curr        
            curr = curr.next

        return dummy.next





        