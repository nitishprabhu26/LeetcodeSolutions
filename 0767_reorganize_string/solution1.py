# Neetcode:
# https://youtu.be/2g_b1aYTHeg

# Intuition:
# Keep adding the most frequest charecter to the output string, and do it until all the charecters are used.
# eg: "aaabc"
# hashmap:{a:3, b:1, c:1}
# now once we add 'a', we need to put 'a' on hold and use the next most frequesnt charecter for the next step.
# then again you can use 'a' since its the most frequent charecter again.
# ans -> "abaca"

# We can use a hashmap to store the count of each charecters given in the input, but using hashmap, to find most
# frequent charecter we need to loop through it everytime. time comp: O(n^2), technically O(26.n) = O(n)
# so efficient way is to:
# instead we can use a maxheap data structure (use minheap in python) => O(logn) to sort


from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # Hashmap, count wach char
        count = Counter(s)
        # we put cnt first, because python does heapify based on the first value in the below list pair
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        # O(n) amortized
        heapq.heapify(maxHeap)

        # to store the previous charecter that we used, so that we dont use it again immediately
        prev = None
        res = ""

        # loop until maxHeap is not empty or previous is not null(if prev is already set)
        # 'or' because initially prev is empty
        while maxHeap or prev:

            # if string is invalid
            # eg: a -> 3, b -> 1
            # "abaa" i.e. if prev is not empty and maxheap is empty
            if prev and not maxHeap:
                return ""

            # most freq, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            # reduce the count by 1
            cnt += 1

            # add it back to heap, if we still have a prev from the last iteration
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # on pop, the char is removed, so we store it in prev to add it back later
            # (while decrementing count by 1, and also while cnt is not 0)
            if cnt != 0:
                prev = [cnt, char]

        return res

s = "aab"
s = "aaab"
obj = Solution()
print(obj.reorganizeString(s))

# Complexity analysis:

# Time complexity : O(n.logn)
# Space complexity : O(n)
