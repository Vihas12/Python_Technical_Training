"""
Graph:
    - A graph is a data structure that consists of a finite set of nodes (or vertices) and a set of edges connecting them.
    -Types of Graph:
        -- Directed Graph
        -- Undirected Graph
    - Cyclic Graph:
        -- A graph that has a cycle.
    - Acyclic Graph:
        -- A graph that has no cycle.
    - Indegree:
        -- The number of edges directed into a node in a directed graph.
    - Outdegree:
        -- The number of edges directed out of a node in a directed graph.
    - Complete Graph:
    - Connected Graph:
        - Fully connected graph.
        - Unconnected graph.
        
        
    o undirected & unweighted graph
                                                                                    | A | B | C | D | E
                      A ----------- B                                             A | 0 | 1 | 0 | 0 | 0               
                      |             |\                                            B | 1 | 0 | 0 | 1 | 1  
                      |             |   E                                         C | 1 | 0 | 0 | 1 | 0
                      |             |/                                            D | 0 | 1 | 1 | 0 | 1
                      C------------ D                                             E | 0 | 1 | 0 | 1 | 0
    
    {
        A: [B, C],
        B: [A, D, E],
        C: [A, D],
        D: [B, C, E],
        E: [B, D]
    }
    
"""

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() :
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B','E')
my_graph.add_edge('C','D')
my_graph.add_edge('D','E')

my_graph.print_graph()
print(my_graph.adjacency_list)

"""
BFS:
    o BFS is an algorithm for traversing Graph data structure. It starts at some arbitrary node of a graph and explores the neighbour nodes (which are at current level ) first, brfore moving to the next level neighbour

DFS:
    o DFS is an algorithm for traversing a grpah data structure which starts selecting some arbitary node and explore as far as possilbe along each edge before backtracking      

"""