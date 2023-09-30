from collections import deque
from constants import *



def is_valid(x, y, grid):

    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != I

def get_next_coordinate(grid, location):


    # Define possible moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize BFS structures
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque([(location, [])])  # Each element in the queue is a tuple of (location, path taken to that location)
    visited[location[0]][location[1]] = True
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Check if current location is a pellet. If so, return the first move from the path.
        if grid[x][y] == o:
            if path:
                return path[0]  # Return the first move to get to the pellet
            return location  # If we're already on a pellet, return current location
        
        # Explore neighboring cells
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, grid) and not visited[new_x][new_y]:
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                visited[new_x][new_y] = True
    
    # If there's no reachable pellet, return current location
    return location
