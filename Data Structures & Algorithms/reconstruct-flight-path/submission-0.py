from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        route = []

        def dfs(airport: str) -> None:
            while adj[airport]:
                next_airport = heapq.heappop(adj[airport])
                dfs(next_airport)
            route.append(airport)

        dfs("JFK")
        return route[::-1]

        