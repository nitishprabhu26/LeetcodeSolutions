# Approach: using array with the given range
# https://youtu.be/-iHThH2Vsxw

class MyHashMap:

    def __init__(self):
        self.l = [ -1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.l[key] = value

    def get(self, key: int) -> int:
        return self.l[key]

    def remove(self, key: int) -> None:
        self.l[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(N).