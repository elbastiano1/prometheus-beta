from collections import deque
from typing import List, Tuple, Optional

def find_shortest_path(grid: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from start to end in a maze.
    
    Args:
        grid (List[List[int]]): A 2D grid where:
            0 represents an empty cell
            1 represents a wall
            2 represents the starting cell
            3 represents the end cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end as a list of coordinates,
        or None if no path exists.
    
    Raises:
        ValueError: If grid is empty or invalid
    """
    # Validate input grid
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Find start and end cells
    start = None
    end = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                start = (r, c)
            elif grid[r][c] == 3:
                end = (r, c)
    
    # Validate start and end exist
    if start is None or end is None:
        raise ValueError("Start (2) or end (3) cell not found in grid")
    
    # If start and end are the same, return just the start cell
    if start == end:
        return [start]
    
    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Explore neighbors
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # 4-directional movement
            next_cell = (current[0] + dx, current[1] + dy)
            
            # Check if next cell is the end
            if next_cell == end:
                # Return path that includes only the most direct route
                result_path = path + [next_cell]
                if result_path[0] == start and result_path[-1] == end:
                    return result_path
            
            # Check if next cell is valid and not visited
            if (is_valid(grid, next_cell) and 
                next_cell not in visited and 
                grid[next_cell[0]][next_cell[1]] != 1):
                queue.append((next_cell, path + [next_cell]))
                visited.add(next_cell)
    
    # No path found
    return None

def is_valid(grid: List[List[int]], cell: Tuple[int, int]) -> bool:
    """
    Check if a cell is within grid boundaries.
    
    Args:
        grid (List[List[int]]): The maze grid
        cell (Tuple[int, int]): Coordinates to check
    
    Returns:
        bool: True if cell is within grid boundaries, False otherwise
    """
    rows, cols = len(grid), len(grid[0])
    r, c = cell
    return 0 <= r < rows and 0 <= c < cols

def get_neighbors(grid: List[List[int]], cell: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get valid neighboring cells.
    
    Args:
        grid (List[List[int]]): The maze grid
        cell (Tuple[int, int]): Current cell coordinates
    
    Returns:
        List[Tuple[int, int]]: List of valid neighboring cells
    """
    neighbors = []
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # 4-directional movement
        next_cell = (cell[0] + dx, cell[1] + dy)
        if is_valid(grid, next_cell) and grid[next_cell[0]][next_cell[1]] != 1:
            neighbors.append(next_cell)
    return neighbors