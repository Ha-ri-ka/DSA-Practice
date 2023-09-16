class Node:
    def __init__(self,data):
        self.data=data   
        self.next=None
#-----------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
    
    def Display(self):
        current=self.head
        while current:
            if(current.next!=None):
                print(f'{current.data}',end="-->")
            else:
                print(current.data)
            current=current.next

    def deleteAtFront(self):
        # newHead=self.head.next
        # self.head=newHead
        self.head=self.head.next

    def deleteAtindex(self,pos):
        if pos==0:
            self.head=self.head.next
        else:
            curr=self.head
            ind=0
            while(ind!=pos-1 and curr):
                curr=curr.next
                ind+=1
            curr.next=curr.next.next


    def deleteAfterValue(self,value):
        curr=self.head
        while(curr.data!=value):      
            curr=curr.next
        curr.next=curr.next.next
#----------------------------------------------------------- 
myList=LinkedList()
myList.append(8)
myList.append(9)
myList.append(11)
myList.append(7)
myList.append(2)
#-----------------------------------------------------------
# print("before deletion at front:")
# myList.Display()
# myList.deleteAtFront()
# print("after deletion at front:")
# myList.Display()
#-----------------------------------------------------------
# deletePos=int(input("Enter index to delete at:"))
# print("before deletion:")
# myList.Display()
# myList.deleteAtindex(deletePos)
# print("after deletion:")
# myList.Display()
#-----------------------------------------------------------
deletePos=int(input("Enter value after which you want to delete:"))
print("before deletion:")
myList.Display()
myList.deleteAfterValue(deletePos)
print("after deletion:")
myList.Display()
