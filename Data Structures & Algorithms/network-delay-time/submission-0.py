from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            max_time = time

            for v, w in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (time + w, v))

        return max_time if len(visited) == n else -1

        