class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        n = len(grid)
        queue = deque()
        
        # Add all land cells to queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_dist = -1
        
        while queue:
            x, y, dist = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1  # Mark as visited
                    max_dist = max(max_dist, dist + 1)
                    queue.append((nx, ny, dist + 1))
        
        return max_dist