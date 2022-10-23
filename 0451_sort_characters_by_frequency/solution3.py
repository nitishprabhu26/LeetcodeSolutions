# Approach 3: Multiset and Bucket Sort
# https://leetcode.com/problems/sort-characters-by-frequency/solution/

# Intuition:
# A way of solving this problem with a time complexity of O(n). 
# Firstly, observe that because all of the characters came out of a String of length n, the maximum frequency for 
# any one character is n. This means that once we've determined all the letter frequencies using a HashMap, we can 
# sort them in O(n) time using Bucket Sort. Recall that for our previous approaches, we used comparison-based 
# sorts, which have a cost of O(nlogn).
# Recall that Bucket Sort is the sorting algorithm where items are placed at Array indexes based on their values 
# (the indexes are called "buckets"). For this problem, we'll need to have a List of characters at each index. 
# While we could simply make our bucket Array length n, we're best to just look for the maximum value (frequency) 
# in the HashMap. That way, we only use as much space as we need, and won't need to iterate over heaps of empty 
# buckets during the next phase.
# Finally, we need to iterate over the buckets, starting with the largest and ending with the smallest, building 
# up the string in much the same way as we did before.


import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return s

        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)


s = "tree"
obj = Solution()
print(obj.frequencySort(s))


# Complexity Analysis:
# Let n be the length of the input String. The k (number of unique characters in the input String that we 
# considered for the last approach makes no difference this time).
# Time Complexity: O(n).
# - Like before, the HashMap building has a cost of O(n).
# - The bucket sorting is O(n), because inserting items has a cost of O(k) (each entry from the HashMap), and 
#   building the buckets initially has a worst case of O(n) (which occurs when k = 1). Because k ≤ n, we're left 
#   with O(n).
# - So in total, we have O(n).
# - It'd be impossible to do better than this, because we need to look at each of the n characters in the input 
#   String at least once.
# Space Complexity: O(n).
# Same as above. The bucket Array also uses O(n) space, because its length is at most n, and there are k items 
# across all the buckets.