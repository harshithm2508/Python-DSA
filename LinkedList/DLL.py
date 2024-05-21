class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self) -> None:
        self.head = None

    # printing DLL                                  TC->O(n) SC->O(1)
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

    
    #   Searching for an element in LL                      TC->O(n) SC->O(1)
    def search(self,ele):
        if not self.head:
            print("Linked List is empty")
            return
        temp = self.head
        while temp is not None:
            if(temp.data == ele):
                print(temp.data)
                return
            else:
                temp = temp.next
        print("Element is not found")


    
    #   Inserting node at the beginning of the DLL
    def insertAtBegin(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

dll = DLL()
dll.insertAtBegin(5)
dll.insertAtBegin(4)
dll.insertAtBegin(3)
dll.insertAtBegin(2)
dll.insertAtBegin(1)
dll.printList()
print(dll.head.prev)