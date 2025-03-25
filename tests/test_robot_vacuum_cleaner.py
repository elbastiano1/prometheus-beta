import pytest
from src.robot_vacuum_cleaner import cleanRoom

def test_basic_room_cleaning():
    # Simple room with all empty cells
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == 8  # Robot should clean all 9 cells

def test_room_with_obstacles():
    # Room with some obstacles
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == 6  # Should clean around the obstacle

def test_impossible_cleaning():
    # Room where not all cells can be reached
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == -1  # Cannot clean all cells

def test_single_cell_room():
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 0)
    assert steps == 0  # Only 1 cell to clean

def test_invalid_start_position():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError, match="Starting position is an obstacle"):
        cleanRoom(grid, 1, 1, 0)

def test_out_of_bounds_start():
    grid = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError, match="Starting position is out of grid bounds"):
        cleanRoom(grid, 2, 0, 0)

def test_invalid_direction():
    grid = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError, match="Invalid direction"):
        cleanRoom(grid, 0, 0, 4)

def test_empty_grid():
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        cleanRoom([], 0, 0, 0)
        cleanRoom([[]], 0, 0, 0)