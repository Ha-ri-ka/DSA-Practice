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

    def addAtFront(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    
    def insertAtIndex(self,data,pos):
        new=Node(data)
        curr=self.head
        ind=0
        while(ind!=pos-1 and curr):
            curr=curr.next
            ind+=1
        new.next=curr.next
        curr.next=new

    def insertAfterValue(self,data,value):
        new=Node(data)
        curr=self.head
        while(curr.data!=value):      
            curr=curr.next
        new.next=curr.next
        curr.next=new
#----------------------------------------------------------- 
myList=LinkedList()
myList.append(8)
myList.append(9)
myList.append(11)
myList.append(7)
myList.append(2)
#-----------------------------------------------------------
# print("before insertion at front:")
# myList.Display()
# myList.addAtFront(69)
# print("after insertion at front:")
# myList.Display()
#-----------------------------------------------------------
# insertVal=int(input("enter value to insert: "))
# insertPos=int(input("Enter index to insert at:"))
# print("before insertion:")
# myList.Display()
# myList.insertAtIndex(insertVal,insertPos)
# print("after insertion:")
# myList.Display()
#-----------------------------------------------------------
insertVal=int(input("enter value to insert: "))
insertPos=int(input("Enter value after which you want to insert:"))
print("before insertion:")
myList.Display()
myList.insertAfterValue(insertVal,insertPos)
print("after insertion:")
myList.Display()
