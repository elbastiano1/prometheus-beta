from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a grid-based room and return the minimum number of steps required.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room layout
        0 represents an empty cell
        1 represents an obstacle
    - r (int): Starting row of the robot
    - c (int): Starting column of the robot
    - direction (int): Initial direction of the robot (0: Up, 1: Right, 2: Down, 3: Left)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room
    
    Raises:
    - ValueError: If input parameters are invalid
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of grid bounds")
    
    if direction < 0 or direction > 3:
        raise ValueError("Invalid direction. Must be 0, 1, 2, or 3")
    
    # Check if starting position is an obstacle
    if grid[r][c] == 1:
        raise ValueError("Starting position is an obstacle")
    
    # Directions: Up, Right, Down, Left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # Track visited cells and steps
    visited = set()
    steps = 0
    
    def dfs(x: int, y: int, curr_dir: int) -> int:
        nonlocal steps
        
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try all 4 directions
        total_steps = 0
        for i in range(4):
            # Calculate next direction and position
            next_dir = (curr_dir + i) % 4
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]
            
            # Check if next position is valid and not visited
            if (0 <= nx < len(grid) and 
                0 <= ny < len(grid[0]) and 
                grid[nx][ny] == 0 and 
                (nx, ny) not in visited):
                
                # Move and increment steps
                steps += 1
                total_steps += dfs(nx, ny, next_dir)
        
        return total_steps
    
    # Run the cleaning algorithm
    dfs(r, c, direction)
    
    # Check if all cells were cleaned
    total_empty_cells = sum(row.count(0) for row in grid)
    
    # If not all cells were cleaned, return -1
    return steps if len(visited) == total_empty_cells else -1