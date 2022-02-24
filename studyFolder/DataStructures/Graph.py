# Adjacency List
# Adjacency Matrix

# Storage Space O(|V|**2)  O(|V|+|E|)
# Adding A Vertex O(|V|**2) require copying whole matrix O(1)
# Adding A Edge O(1) O(1)
# Removing a vertex O(|V|**2) require copying whole matrix O(|V|+|E|)
# Removing an edge O(1) O(|V|)
# Querying O(1) O(|V|)
# If graph is sparse use list if not use matrix

class adjancy_list():

    adj_list = {}

    def __init__(self):
    #Adding nodes
        self.add_node(0)
        self.add_node(1)
        self.add_node(2)
        self.add_node(3)
        self.add_node(4)
        #Adding edges
        self.add_edge(0,1)
        self.add_edge(1,2)
        self.add_edge(2,3)
        self.add_edge(3,0)
        self.add_edge(3,4)
        self.add_edge(4,0)
        
        #Printing the graph
        self.graph()
        
        #Printing the adjacency list
        print(self.adj_list)

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        # Assume node1 and node2 are in adj_list
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def graph(self):
        for node in self.adj_list:
            print(node, " ---> ", [i for i in self.adj_list[node]])
    
class adjancy_matrix:
    adj_mat = []
    
    def __init__(self):
        #Adding nodes
        self.add_node(0)
        self.add_node(1)
        self.add_node(2)
        self.add_node(3)
        self.add_node(4)
        #Adding edges
        self.add_edge(0,1)
        self.add_edge(1,2)
        self.add_edge(2,3)
        self.add_edge(3,0)
        self.add_edge(3,4)
        self.add_edge(4,0)
        
        #Printing the adjacency list
        print(self.adj_mat)

    def add_node(self, node):
        self.adj_mat.append([0]*len(self.adj_mat))
        for row in self.adj_mat:
            row.append(0)
    
    def add_edge(self, node1, node2):
        self.adj_mat[node1][node2] = 1
        self.adj_mat[node2][node1] = 1

if __name__ == "__main__":
    adjancy_list()
    adjancy_matrix()