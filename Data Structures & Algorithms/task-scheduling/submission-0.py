from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # Stores (remaining_count, ready_time)

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)  # Decrement negative count
                if cnt < 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time

        