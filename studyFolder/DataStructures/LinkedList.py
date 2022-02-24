# LinkedList class is to help with abstraction
class LinkedList:
    def __init__(self):
        self.head = None

# could just use Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def traverseThrough(linked_list):
    head = linked_list.head
    while (head != None):
        print(head.data)
        head = head.next

def messingAround():
    linked_list = LinkedList()
    node = Node(0)
    linked_list.head = node
    for i in range(1,10):
        node.next = Node(i)
        node = node.next
    traverseThrough(linked_list)

if __name__ == "__main__":
    messingAround()
# Circular Linked List

# Operations

# Depends on whether I have the node or not
# Traversal O(n)
# Insertion O(1) front
# Deletion O(n)
# Searching O(n)
# Updating O(n)
# Sorting O(nlogn)
# Merging O(n)