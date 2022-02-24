# BFS/DFS for Binary Tree
# BFS/DFS for Graph

'''
BFS O(V+E)
DFS O(V+E)

'''

import sys

sys.path.append('D:\Jackson\leetcodeChallenges\studyFolder')


from DataStructures.Graph import adjancy_list, adjancy_matrix
from DataStructures.Tree import *
from collections import deque

# BFS for adjancy_list

def BFS():
    adj_list = adjancy_list().adj_list
    start = list(adj_list.keys())[0]
    visited = {}
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while (queue):
        start = queue.popleft()
        for nodes in adj_list[start]:
            if nodes not in visited:
                visited[nodes] = 1
                queue.append(nodes)
        print(start)

def DFS():
    pass


BFS()