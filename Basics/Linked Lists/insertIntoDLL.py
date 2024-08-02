# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    if not head.next:
        head.next=Node(data)
        head.next.prev=head
        return head
    temp=head
    pos=0
    while(pos!=p):
        temp=temp.next
        pos+=1
    new=Node(data)
    new.next=temp.next
    new.prev=temp
    temp.next=new
    if new.next:
        new.next.prev=new
    return head
