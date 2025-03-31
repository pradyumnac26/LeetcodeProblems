# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # so what i can do here is. 
        # given x, traverse through the list and find elements lesser than x and push them say to an array. 
        # then convert that array to ll , and then the remaining arrayjust push after this. its like breaking the ll into 2 lists and then combining them to mae a ll.
        temp = head
        less = [] 
        great = [] 
        while temp != None : 
            if temp.val < x : 
                less.append(temp.val)
            else : 
                great.append(temp.val)
            temp = temp.next
        print(less)
        print(great)
        z = head
        i = 0 
        while i < (len(less)) : 
            z.val = less[i]
            print(z.val)
            i = i+1
            z = z.next
        i = 0 
        while i < len(great) : 
            z.val = great[i]
            print(z.val)
            i = i+1
            z = z.next
        return head



        