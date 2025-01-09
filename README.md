# Implement-Linked-List
 implement a few methods of the class LinkedList
 which implements the linked list data structure. Use the existing methods of the LinkedList class to
 help implement the required methods.
 You will be provided a LinkedList class. The class includes various methods you to help you complete
 the assignment:
 • llist = LinkedList(): Constructs a LinkedList object. Each linked list is constructed of
 Node() objects.
 • llist.head returns the pointer to the head node of the linked list.
 • llist.insertAtBegin(self, data) adds a node to the beginning of the linked list with a value
 of data.
 • llist.insertAtIndex(self, data, index) adds a node at index. Indexing starts from 0.
 • llist.insertAtEnd(self, data) adds a node to the end of the linked list with a value of data.
 • llist.updateNode(self, val, index) updates the node at index to the value val.
 • llist.sizeOfLL(self) returns the size of the linked list (number of nodes).
 You will be provided a Node class. The node class only contains two attributes and no methods. Node
 objects construct a linked list.
 • node = Node(): Constructs a Node object.
 • node.data returns the value stored at the current node.
 • node.next returns the pointer to the next node in the linked list.
  Merge
 Description: Implement the method merge(self, llist2) that merges two sorted singly linked lists
 together. The method must merge the nodes in place. This means that the reversal must be performed
 within the existing linked list structure without instantiating any new node or linked list objects. The
 result must add all the nodes from the llist2 object that is passed to the method into the linked list
 the method is called on. The resulting merged linked list must maintain the sorted order after merging.
