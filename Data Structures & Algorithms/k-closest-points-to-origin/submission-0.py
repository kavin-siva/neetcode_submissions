import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, [x, y]))
            else:
                heapq.heappushpop(max_heap, (dist, [x, y]))

        return [point for _, point in max_heap]

        