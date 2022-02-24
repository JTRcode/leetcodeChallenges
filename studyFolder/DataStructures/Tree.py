'''
Tree
Binary Tree
Binary Search Tree
AVL Tree
Red Black Tree

Binary Search Tree
Searching avg:O(logn or height) depends on how balanced. worst:O(n)
Insertion avg:O(logn or height) depends on how balanced. worst:O(n)
Deletion avg:O(logn or height) depends on how balanced. worst:O(n)

Preorder
Postorder
Inorder

'''

from contextlib import nullcontext
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def DFS_iterative(head):
    stack = []
    explored = [] # Better to have each node have a id so I can use a dictionary or something 
    stack.append(head)
    explored.append(head)
    node = head
    while(len(stack)):
        node = stack.pop()
        if (node.left != None and node.left not in explored): 
            stack.append(node.left)
            explored.append(node.left)
        if (node.right != None and node.right not in explored):
            stack.append(node.right)
            explored.append(node.right)
        print(node.data)

def DFS_recursive(head):
    if (head == None):
        return 
    DFS_recursive(head.left)
    DFS_recursive(head.right)
    print(head.data)

def BFS_iterative(head):
    queue = deque() # deque has pop(0) O(1) time complexity when [] has O(n)
    queue.append(head)
    while (queue):
        node = queue.popleft()
        if (node.left != None): queue.append(node.left)
        if (node.right != None): queue.append(node.right)
        print(node.data)

def messingAround():
    head = Node(5)
    leftChild = Node(3)
    leftChild.right = Node(4)
    leftChild.left = Node(-2)
    head.left = leftChild
    head.right = Node(10)
    # DFS_recursive(head)
    BFS_iterative(head)

if __name__ == "__main__":
    messingAround()
