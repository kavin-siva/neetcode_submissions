from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_len = len(beginWord)
        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            curr_word, steps = queue.popleft()
            for i in range(word_len):
                pattern = curr_word[:i] + "*" + curr_word[i + 1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                pattern_map[pattern].clear()  # Avoid revisiting the same pattern

        return 0

        