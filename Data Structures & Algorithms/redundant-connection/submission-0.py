class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(u: int, v: int) -> bool:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False

            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []

        