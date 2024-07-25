# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # length=0
        # temp=head
        # while(temp):
        #     length+=1
        #     temp=temp.next
        # mid=(length/2)+1
        # index=1
        # temp=head
        # while(index!=mid):
        #     temp=temp.next
        #     index+=1
        # return temp

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
