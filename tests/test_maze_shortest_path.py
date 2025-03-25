import pytest
from src.maze_shortest_path import find_shortest_path, is_valid, get_neighbors

def test_simple_path():
    """Test a simple maze with a direct path"""
    grid = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 2  # Start to end
    assert path[0] == (1, 0)  # Start cell
    assert path[1] == (1, 2)  # End cell

def test_path_with_obstacles():
    """Test a maze with obstacles requiring navigation"""
    grid = [
        [0, 0, 0, 0],
        [2, 1, 0, 3],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 7  # Navigating around obstacles
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (1, 3)  # End cell

def test_no_path_exists():
    """Test a maze where no path exists"""
    grid = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3]
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_start_end_same_cell():
    """Test when start and end are the same cell"""
    grid = [
        [0, 0, 0],
        [0, 2, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 1
    assert path[0] == (1, 1)

def test_empty_grid():
    """Test empty grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_no_start_or_end():
    """Test grid without start or end cell raises ValueError"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError):
        find_shortest_path(grid)

def test_is_valid():
    """Test is_valid function"""
    grid = [
        [0, 0, 0],
        [0, 2, 3],
        [0, 0, 0]
    ]
    assert is_valid(grid, (0, 0)) == True
    assert is_valid(grid, (2, 2)) == True
    assert is_valid(grid, (-1, 0)) == False
    assert is_valid(grid, (3, 0)) == False
    assert is_valid(grid, (0, 3)) == False

def test_get_neighbors():
    """Test get_neighbors function"""
    grid = [
        [0, 0, 0],
        [0, 2, 1],
        [0, 0, 0]
    ]
    neighbors = get_neighbors(grid, (1, 1))
    assert len(neighbors) == 3
    assert (1, 0) in neighbors
    assert (2, 1) in neighbors
    assert (0, 1) in neighbors