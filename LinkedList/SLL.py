class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        else:
            new_node.next = self.head
