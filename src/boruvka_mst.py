from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set data structure for tracking connected components 
    in Boruvka's Minimum Spanning Tree algorithm.
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with given number of vertices.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of a set using path compression.
        
        Args:
            item (int): Vertex to find root for
        
        Returns:
            int: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Union two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union is successful, False if already in same set
        """
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

        return True

def boruvka_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find Minimum Spanning Tree.
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges in the format (u, v, weight)
    
    Returns:
        List[Tuple[int, int, int]]: Edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If input is invalid
    """
    # Input validation
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        raise ValueError("Edge list cannot be empty")

    # Special case for single vertex
    if vertices == 1:
        return []

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # Result MST
    mst = []
    
    # Number of unique components
    components = vertices
    
    # Boruvka's algorithm main loop
    while components > 1:
        selected_edges = []
        components_edges = {}
        
        # Find cheapest edge for each component
        for u, v, weight in edges:
            root_u = ds.find(u)
            root_v = ds.find(v)
            
            if root_u != root_v:
                if (root_u not in components_edges or 
                    weight < components_edges[root_u][2]):
                    components_edges[root_u] = (u, v, weight)
                
                if (root_v not in components_edges or 
                    weight < components_edges[root_v][2]):
                    components_edges[root_v] = (u, v, weight)
        
        # Add selected edges
        for edge in components_edges.values():
            u, v, weight = edge
            if ds.union(u, v):
                mst.append(edge)
                components -= 1
        
        # Break if no more edges can be added
        if not components_edges:
            break
    
    return mst