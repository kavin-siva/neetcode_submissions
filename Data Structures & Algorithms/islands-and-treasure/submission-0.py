from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r: int, c: int) -> None:
            if (
                r < 0 or r == ROWS or c < 0 or c == COLS
                or (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        # 1. Enqueue all treasure chests (0s) as simultaneous BFS sources
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # 2. Expand outward layer by layer
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        