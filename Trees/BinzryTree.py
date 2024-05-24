class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def TreeInorder(root):
    if root==None:
        return None
    TreeInorder(root.left)
    print(root.data,end="")
    TreeInorder(root.right)

def TreePreorder(root):
    if root==None:
        return None
    print(root.data,end="")
    TreePreorder(root.left)
    TreePreorder(root.right)

def TreePostorder(root):
    if root==None:
        return None
    TreePreorder(root.left)
    TreePreorder(root.right)
    print(root.data,end="")

def TreeLevelorder(root):
    if root==None:
        return None
    result=[]
    q=[root]
    while len(q)>0:
        n=len(q)
        sub=[]
        
        for i in range(n):
            curr=q.pop(0)
            sub.append(curr.data)
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
        result.append(sub)
    return result

root=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
n5=Node(6)
n6=Node(7)
root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
n2.left=n5
n2.right=n6

print("Inorder Traversal")
TreeInorder(root)
print()
print("Preorder Traversal")
TreePreorder(root)
print()
print("Postorder Traversal")
TreePostorder(root)
print()
print("Levelorder Traversal")
print(TreeLevelorder(root))