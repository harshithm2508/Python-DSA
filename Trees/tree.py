class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


#   Inorder Traversal
def printInOrderTraversal(root):
    if root == None:
        return

    printInOrderTraversal(root.left)
    print(root.data, end=" ")
    printInOrderTraversal(root.right)


#   Preorder Traversal
def printPreOrderTraversal(root):
    if root == None:
        return

    print(root.data,end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)


#   Post order traversal
def printPostOrderTraversal(root):
    if root == None:
        return

    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data,end=" ")



#   LevelOrder traversal
def levelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
 
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)
 
    print(result)


#   Finding left view
def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]

    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
    return result

def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    




obj1 = Node(1)
obj2 = Node(2)
obj3 = Node(3)
obj4 = Node(4)
obj5 = Node(5)

obj1.left = obj2
obj1.right = obj3
obj2.left = obj4
obj2.right = obj5
printInOrderTraversal(obj1)
print()
printPreOrderTraversal(obj1)
print()
printPostOrderTraversal(obj1)
print()
levelOrderTraversal(obj1)