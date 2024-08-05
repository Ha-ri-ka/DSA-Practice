class Node:
    def __init__(self,data=None) -> None:
        self.data=data
        self.left=None
        self.right=None

def createTree():
    newNode=Node()
    try:
        data=int(input(""))
    except ValueError:
        return
    # if data==-1:
    newNode.data=data
    print(f"Enter left child of {data}",end=" ")
    newNode.left=createTree()
    print(f"Enter right child of {data}",end=" ")
    newNode.right=createTree()
    return newNode   

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")

print("enter data to create node\nEnter any non-numeric key to cancel node creation")
root=createTree()
print("Inorder traversal:")
inorder(root)
print("\nPreorder traversal:")
preOrder(root)
print("\nPostorder traversal:")
postOrder(root)
