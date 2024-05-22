class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self) -> None:
        self.head = None

    def size(self):
        temp = self.head
        len = 0
        while(temp is not None):
            len += 1
            temp = temp.next
        return len

    # printing DLL                                  TC->O(n) SC->O(1)
    def printList(self):
        print("None <-",end=" ")
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


    
    #   Inserting node at the beginning of the DLL          TC -> O(1) SC->O(1)
    def insertAtBegin(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    
    #   Inserting node at the end of DLL                    TC-> O(n) SC->O(1)
    def insertAtTail(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last


    #   Inserting at a position in DLL
    #   Correct this code
    def insertAtPos(self, data, pos):
        if pos < 0 or pos > self.size():
            print("Position is invalid")
            return

        new_node = Node(data)

        if pos == 0:
            self.insertAtBegin(data)
            return
        elif pos == self.size():
            self.insertAtTail(data)
            return

        temp = self.head
        for i in range(pos - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node



    #   Delete at head
    def deleteAtHead(self):
        if self.head is None:
            print("Nothing to delete. DLL is empty.")
            return
        
        self.head = self.head.next

    
    #   Delete at Tail
    def deleteAtTail(self):
        if self.head is None:
            print("Nothing to delete. DLL is empty.")
            return
        temp = self.head
        while(temp.next.next is not None):
            temp = temp.next
        temp.next = None


dll = DLL()
dll.insertAtBegin(5)
dll.insertAtBegin(3)
dll.insertAtBegin(2)
dll.insertAtBegin(1)
dll.insertAtTail(6)
dll.insertAtTail(7)
dll.insertAtPos(4,4)
dll.deleteAtHead()
dll.deleteAtTail()
print(dll.size())
dll.printList()