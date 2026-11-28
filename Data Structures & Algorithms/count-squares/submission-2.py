from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.pts_count = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        px, py = point
        res = 0

        for (x, y), cnt in self.pts_count.items():
            if abs(px - x) != abs(py - y) or px == x:
                continue

            res += cnt * self.pts_count.get((px, y), 0) * self.pts_count.get((x, py), 0)

        return res


        
