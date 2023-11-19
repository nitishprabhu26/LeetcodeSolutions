# Approach: Using Arrays and Sort


from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        self.arr.sort()

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[-self.k]
        

# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))


# Complexity Analysis:
# Time complexity : O(N.log N).
# Space complexity : O(N) to store the values in array.