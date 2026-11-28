from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for start in sorted(count):
            need = count[start]
            if need > 0:
                for card in range(start, start + groupSize):
                    if count[card] < need:
                        return False
                    count[card] -= need

        return True

        