class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self) -> None:
        self.head = None

    #   Printing the Linked List                            TC->O(n) SC->O(1)
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
    

    #   Inserting node at the beginning of the LL           TC->O(1) SC->O(1)
    def insertAtBegin(self,data):
        new_node = Node(data)

        if not(self.head):
            self.head = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
    

    #   Inserting node at the end of the LL                 TC->O(n) SC->O(1)
    def insertAtTail(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node


    #   Inserting node at a particular position in LL        TC->O(n) SC->O(1)
    def insertAtPos(self,data,pos):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        for i in range(pos-2):
            temp = temp.next 
        new_node.next = temp.next
        temp.next = new_node


    #   Deletion of the head                                 TC->O(1) SC->O(1)
    def deleteAtHead(self):
        if self.head is None:
            print("There is no head to delete. LL is empty")
        self.head = self.head.next

    
    #   Deletion of the tail node                            TC->O(n) SC->O(1)
    def deleteAtTail(self):
        if self.head is None:
            print("There is no tail node to delete. LL is empty")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    #   Deletion at a specific node                             TC->O(n) SC->O(1)
    def deleteAtPos(self,pos):
        if not self.head:
            print("There is no tail node to delete. LL is empty")
            return
        
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        temp.next = temp.next.next
        


n1 = SLL()
n1.insertAtBegin(5)
n1.insertAtBegin(4)
n1.insertAtBegin(2)
n1.insertAtBegin(1)
n1.insertAtPos(3,3)
n1.insertAtPos(7,6)
n1.deleteAtTail()
n1.deleteAtPos(4)
n1.printList()
n1.search(1)