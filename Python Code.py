class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node and position != index:
                position += 1
                current_node = current_node.next

            if current_node:
                current_node.data = val
            else:
                print("Index not present")

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print method for the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # The code below will remove all duplicate nodes from the linked list
    def remove_duplicates(self):
        if not self.head:  
            return
        
        first_occurance = set()
        current_node = self.head
        first_occurance.add(current_node.data)

        while current_node.next:
            if current_node.next.data in first_occurance:
                current_node.next = current_node.next.next  
            else:
                first_occurance.add(current_node.next.data)
                current_node = current_node.next

    # The code below will merge all nodes from llist2 into the linked list object
    def merge(self, llist2):
        if not self.head:
            self.head = llist2.head
            return
        if not llist2.head:
            return

        duplicate1 = Node(0)
        end = duplicate1
        first_Node = self.head
        second_Node = llist2.head

        while first_Node and second_Node:
            if first_Node.data <= second_Node.data:
                end.next = first_Node
                first_Node = first_Node.next
            else:
                end.next = second_Node
                second_Node = second_Node.next
            end = end.next

        if first_Node:
            end.next = first_Node
        if second_Node:
            end.next = second_Node

        self.head = duplicate1.next

def main():
    llist_nodes = input().split()
    if llist_nodes[0] == 'duplicate':
        llist = LinkedList()
        for i in range(1, len(llist_nodes)):
            llist.insertAtEnd(int(llist_nodes[i]))
        llist.remove_duplicates()
        llist.printLL()
    else:
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist2_index = llist_nodes.index("llist2")
        for i in range(1, llist2_index):
            llist1.insertAtEnd(int(llist_nodes[i]))
        for i in range(llist2_index + 1, len(llist_nodes)):
            llist2.insertAtEnd(int(llist_nodes[i]))
        llist1.merge(llist2)
        llist1.printLL()

if __name__ == "__main__":
    main()
