import numpy as np

# TODO Define graph structure
class graph:
    def __init__(self, node, info, adj_matrix, list_neighbors):
        self.node = node # node = [1, 2, 3, ...]
        self.info = info # info = [[0, 0], [0, 1], ...]
        self.adj_matrix = adj_matrix # How to find the adj_matrix
        self.list_neighbors = list_neighbors
        pass
    
    def get_min_distance(self):
        min_dist = np.inf
        
        for v in self.get_len():
            if 
        pass
    
    def shortest_path(self, source):
        '''
        for each vertex v in Graph.Vertices:
            dist[v] ← INFINITY
            add v to Q
        dist[source] ← 0
        '''
        dist_nodes = np.inf * np.ones(self.get_len())
        set_nodes = self.node
        
        dist_nodes[source] = 0
        
        '''
        while Q is not empty:
            u ← vertex in Q with min dist[u]
            remove u from Q
 
            for each neighbor v of u still in Q:
                alt ← dist[u] + Graph.Edges(u, v)
                if alt < dist[v]:
                    dist[v] ← alt
                    prev[v] ← u
        '''
        
        while set_nodes:
            for node in set_nodes:
                if dist_nodes[node] < min(dist_nodes):
                    current_node = set_nodes.pop(node)
                    
                
            
        pass
    
    def len_vertex_set(self):
        return len(self.node)
    
    def add_node(self, new_node, new_edges):
        self.node.append(new_node)
        self.modify_adj_matrix(new_edges)
        pass
    
    def modify_adj_matrix(self, new_edges):
        self.adj_matrix = []
        pass
    
    def remove_node(self, location):
        self.remove_edge(location)
        pass
    
    def remove_edge(self, location):
        pass
    
    def modify_node(self, new_node):
        pass
    
    def get_len(self):
        return len(self.node)
    
    def get_info(self, node):
        return self.info(node)

node = range(3*3)
'''
Graph
0 - 1 - 2
|   |   |
3 - 4 - 5
|   |   |
6 - 7 - 8

Assume 7 is fatal state
'''
info = np.matrix([[0, 0],[0, 1], [0, 2],
                  [1, 0],[1, 1], [1, 2],
                  [2, 0],[2, 1], [2, 2]])

# Connections
adj_matrix = np.matrix([[0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0]])

list_neighbors = ((1, 3), 
                  (0, 2, 4),
                  (1, 4, 5),
                  (0, 4, 6),
                  (1, 3, 5, 7),
                  (2, 4, 8),
                  (3, 7),
                  (4, 6, 8),
                  (5, 7))

# Cost to fatal state
adj_matrix = np.matrix([[0]])

sample_graph = graph(node, info, adj_matrix, list_neighbors)

sample_graph.shortest_path(0)