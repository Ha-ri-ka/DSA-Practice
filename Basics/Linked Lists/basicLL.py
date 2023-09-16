class Node:
    def __init__(self,data): #self is the node
        self.data=data #it has an attribute of data 
        self.next=None #and a pointer to the next node

class LinkedList:
    def __init__(self):
        self.head=None #attribute of a linked list is its HEAD it identifies a LL
    
    def append(self,data):
        new_node=Node(data)
        #if its empty ll add it as head
        if self.head==None:
            self.head=new_node
        #else look for the last node and add it next to THAT
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

myFirstEverPythonLinkedList=LinkedList()
#hard code
# myFirstEverPythonLinkedList.append(1)
# myFirstEverPythonLinkedList.append(2)
# myFirstEverPythonLinkedList.append(3)
# myFirstEverPythonLinkedList.append(4)
# myFirstEverPythonLinkedList.append(5)
#user input 
print("Enter head to stat creating linked list enter -1 to stop.")
value=int(input("give head:"))
while(value!=-1):
    myFirstEverPythonLinkedList.append(value)
    value=int(input("enter value: "))

myFirstEverPythonLinkedList.Display()         
