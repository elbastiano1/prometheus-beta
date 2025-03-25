import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

class TestBoruvkaMST:
    def test_simple_graph(self):
        """
        Test a simple graph with a known minimum spanning tree
        """
        vertices = 4
        edges = [
            (0, 1, 10),  # Edge between 0 and 1 with weight 10
            (0, 2, 6),   # Edge between 0 and 2 with weight 6
            (0, 3, 5),   # Edge between 0 and 3 with weight 5
            (1, 3, 15),  # Edge between 1 and 3 with weight 15
            (2, 3, 4)    # Edge between 2 and 3 with weight 4
        ]
        
        mst = boruvka_mst(vertices, edges)
        
        # Validate MST total edges and total weight
        assert len(mst) == vertices - 1
        
        # Expected edges (not in specific order)
        expected_edges = {
            (0, 3, 5),  # First selected edge
            (0, 2, 6),  # Second selected edge
            (2, 3, 4)   # Third selected edge
        }
        
        # Convert MST to set for unordered comparison
        mst_set = set(mst)
        assert mst_set == expected_edges

    def test_invalid_vertices(self):
        """
        Test invalid number of vertices
        """
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            boruvka_mst(0, [(0, 1, 10)])
        
        with pytest.raises(ValueError, match="Number of vertices must be positive"):
            boruvka_mst(-1, [(0, 1, 10)])

    def test_empty_edges(self):
        """
        Test empty edge list
        """
        with pytest.raises(ValueError, match="Edge list cannot be empty"):
            boruvka_mst(4, [])

    def test_single_vertex(self):
        """
        Test graph with single vertex
        """
        mst = boruvka_mst(1, [(0, 0, 1)])
        assert len(mst) == 0

    def test_disjoint_set(self):
        """
        Test DisjointSet operations
        """
        ds = DisjointSet(5)
        
        # Test initial state
        for i in range(5):
            assert ds.find(i) == i
        
        # Perform unions
        assert ds.union(0, 1) == True  # First union
        assert ds.union(2, 3) == True  # Second union
        
        # Verify root after union
        assert ds.find(0) == ds.find(1)
        assert ds.find(2) == ds.find(3)
        
        # Repeated union should return False
        assert ds.union(0, 1) == False

    def test_complex_graph(self):
        """
        Test more complex graph
        """
        vertices = 6
        edges = [
            (0, 1, 4), (0, 2, 3), (1, 2, 1),
            (1, 3, 2), (2, 3, 5), (2, 4, 6),
            (3, 4, 7), (3, 5, 4), (4, 5, 8)
        ]
        
        mst = boruvka_mst(vertices, edges)
        
        # Validate MST total edges and total weight
        assert len(mst) == vertices - 1
        
        # Verify minimum total weight algorithm
        mst_weight = sum(edge[2] for edge in mst)
        assert mst_weight == 15  # Minimum possible spanning tree weight