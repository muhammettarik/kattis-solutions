from collections import deque

def solve(n, m, grid):
    q = deque([(0, 0, 0)])
    visited = set((0, 0))

    while q:
        x, y, steps = q.popleft()
        if x == n - 1 and y == m - 1:
            return steps
        k = int(grid[x][y])
        for dx, dy in [(0, k), (k, 0), (0, -k), (-k, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, steps + 1))

    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    result = solve(n, m, grid)
    print(result)
