import numpy as np

# TODO Define graph structure
class graph:
    def __init__(self, node, info, cost, adj_matrix):
        self.node = node
        self.info = info
        self.cost = cost
        self.adj_matrix = adj_matrix
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

# TODO Use for Shortest path
class tree:
    def __init__(self, graph, source):
        self.graph = graph
        self.sourse = []
        self.ancestor = []
        self.descendant = []
        
        self.set_source(source)
        pass

    def set_source(self, source):
        '''
        # Initialization
        for each vertex v in graph.verices:
            dist[v] <- infinity
            prev[v] <- undefined
            
            # Create the vertex set
            add v to Q
        '''
        self.sourse = source
        
        self.ancestor = np.nan * np.ones(self.graph.get_len())
        self.dist = np.inf * np.ones(self.graph.get_len())
        
        self.set_nodes = self.graph.node
        
        '''
        # Distance from source to source    
        dist[source] <- 0
        '''
        self.dist[self.source] = 0

    def add_descendant(self, descendant):
        self.descendant.append(descendant)

    def set_ancestor(self, ancestor):
        self.ancestor = ancestor

    def get_source(self):
        return self.source

    def get_ancestor(self):
        return self.ancestor

    def get_descendant(self):
        return self.descendant

    def short_path(self):
        '''
        Pseudocode for Dijkstra algorithm
        input: graph, source_vertex
        output: vector_distance, vector_previous_nodes
        '''      
        
        '''
        # Compute shortest path
        while Q is non empty:
            # Get new vertex to compute
            u <- vertex in Q with min dist[u]
            remove u from Q
            
            # Compute distance from current vertex to neighbors
            for each neighbor v of u still in Q:
                alt <- dist[u] + graph.edges(u, v)
                if alt < dist[v]:
                    dist[v] <- alt
                    prev[v] <- u
                    
        return dist[], prev[]
        '''
        while self.set_nodes:
            node = self.nodes.pop()
            
            for 
            pass 
        
        pass