class Node:
    def __init__(self,data): 
        self.data=data  
        self.next=None 

class LinkedList:
    def __init__(self):
        self.head=None 
    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
        
    def Display(self):
        current=self.head
        while current:
            if(current.next!=None):
                print(f'{current.data}',end="-->")
            else:
                print(current.data)
            current=current.next
    
    def reverse(self):
        prev,cur=self.head,self.head
        nextNode=cur.next
        self.head.next=None
        prev=cur
        cur=nextNode
        nextNode=cur.next
        while(nextNode.next!=None):
            cur.next=prev
            prev=cur
            cur=nextNode
            nextNode=cur.next
        # print(prev.data,cur.data,next.data)
        # print(prev.next.data,cur.next.data,next.data)
        cur.next=prev
        self.head=nextNode
        self.head.next=cur
    
    def betterReverse(self):
        prev,cur=None,self.head
        while cur:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode
        self.head=prev

myList=LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
print("Before reversing:")
myList.Display()
print("After reversing:")
myList.reverse()
myList.Display()         
