class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def insertIntoBST(root,val):
    if root==None:
        return Node(val)
    elif root.data>val:
        root.left=insertIntoBST(root.left,val)
    else:
        root.right=insertIntoBST(root.right,val)
    return root

def PrintTree(root):
    if root==None:
        return None
    q=[root]
    while len(q)!=0:
        n=len(q)
        for i in range(n):
            curr=q.pop(0)
            print(curr.data,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
        print()

l=[4,2,7,1,3]
root=None
for i in l:
    root=insertIntoBST(root,i)
PrintTree(root)