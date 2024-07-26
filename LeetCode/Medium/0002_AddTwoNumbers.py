# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=ListNode()
        head=None
        carry=0
        sumVal=0
        while l1 and l2:
            sumVal=l1.val+l2.val+carry
            nodeVal=int(sumVal%10)
            carry=int(sumVal/10)
            if head is None:
                head=ListNode()
                head.val=nodeVal
                head.next=None
                curr=head
            else:
                Node=ListNode(nodeVal)
                curr.next=Node
                curr=Node
            l1=l1.next
            l2=l2.next
        if l1 is None and l2:
            while(l2):
                sumVal=l2.val+carry
                nodeVal=int(sumVal%10)
                carry=int(sumVal/10)
                Node=ListNode(nodeVal)
                curr.next=Node
                curr=Node
                l2=l2.next
        if l2 is None and l1:
            while(l1):
                sumVal=l1.val+carry
                nodeVal=int(sumVal%10)
                carry=int(sumVal/10)
                Node=ListNode(nodeVal)
                curr.next=Node
                curr=Node
                l1=l1.next
        if carry!=0:
            curr.next=ListNode(carry)
        return head
