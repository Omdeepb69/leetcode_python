"""
Leetcode 200 (Number of Islands)

Leetcode 695 (Max Area of Island)

Leetcode 733 (Flood Fill)

Leetcode 130 (Surrounded Regions)

Leetcode 417 (Pacific Atlantic Water Flow)   
"""

def dfs(grid, r, c):
    # 1. Boundary and base condition
    if (r < 0 or r >= len(grid) or
        c < 0 or c >= len(grid[0]) or
        grid[r][c] != '1'):   # customize condition
        return

    # 2. Mark as visited
    grid[r][c] = '0'  # customize how you mark it

    # 3. Visit 4 directions (Right, Down, Left, Up)
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:  # can add diagonals
        dfs(grid, r + dr, c + dc)

def bfs(grid, r, c):
    queue = deque()
    queue.append((r, c))
    grid[r][c] = '0'  # mark visited

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] == '1'):  # customize
                grid[nx][ny] = '0'  # mark visited
                queue.append((nx, ny))


def solveGrid(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    result = 0  # or [] if collecting something

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1'):
            return
        grid[r][c] = '0'  # visited
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # starting condition
                dfs(r, c)
                result += 1        # problem-specific logic

    return result
