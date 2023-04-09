# Approach: Neetcode (Using Linked List; chaining)
# https://youtu.be/cNWsgbKwwoU

class ListNode:
    def __init__(self, key=-1, val=-1, next= None):
        self.key = key
        self.val = val
        self.next = next
    
class MyHashMap:

    def __init__(self):
        self.map = [ ListNode() for i in range(1000)]
    
    def hash(self, key):
        return key % len(self.map)
    
    def put(self, key: int, value: int) -> None:
        # two cases: inserting for first time OR if key already exixts
        cur = self.map[self.hash(key)]
        while cur.next:
            # 2nd case: if key already exixts
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # 1st case: if we dont find the key in the list, and we reach the end
        # we insert a new ListNode
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # .next -> since we can skip the dummy node
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)