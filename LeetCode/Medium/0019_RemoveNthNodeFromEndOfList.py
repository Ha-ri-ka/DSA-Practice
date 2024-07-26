# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length=0
        # temp=head
        # while(temp):
        #     length+=1
        #     temp=temp.next
        # index=(length-n)+1
        # if index==1:
        #     return head.next
        # temp=head
        # count=1
        # while(temp):
        #     count+=1
        #     prev=temp
        #     temp=temp.next
        #     if count==index:
        #         prev.next=temp.next
        #         break
        # return head
      
        if not head: 
            return head
        slow=head
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return slow.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head        
