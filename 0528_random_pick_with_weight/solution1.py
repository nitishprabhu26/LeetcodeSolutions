# Approach: Creating a weight list [Wrong answer]

import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.weights = w
        self.weight_list = []
        total = sum(w)
        for weight in w:
            probability = weight / total
            weight_count = round(probability * total)
            
            for _ in range(weight_count):
                self.weight_list.append(weight)

    def pickIndex(self) -> int:
        element = random.choice(self.weight_list)
        return self.weights.index(element)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()