class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            curr = -1
            # Find the unvisited node with the smallest edge cost to the MST
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            visited[curr] = True
            total_cost += min_dist[curr]

            # Update minimum distances to all remaining unvisited nodes
            x1, y1 = points[curr]
            for nxt in range(n):
                if not visited[nxt]:
                    x2, y2 = points[nxt]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[nxt]:
                        min_dist[nxt] = dist

        return total_cost


        