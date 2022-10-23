# Approach 2: HashMap and Sort
# https://leetcode.com/problems/sort-characters-by-frequency/solution/

# Intuition:
# - Another approach is to use a HashMap to count how many times each character occurs in the String; the keys are 
#   characters and the values are frequencies.
# - Next, extract a copy of the keys from the HashMap and sort them by frequency using a Comparator that looks at 
#   the HashMap values to make its decisions.
# - Finally, initialise a new StringBuilder and then iterate over the list of sorted characters (sorted by 
#   frequency). Look up the values in the HashMap to know how many of each character to append to the StringBuilder.


# with counter and most_common() method

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count up the occurances.
        counts = collections.Counter(s)
        
        # Build up the string builder.
        string_builder = []
        for letter, freq in counts.most_common():
            # letter * freq makes freq copies of letter.
            # e.g. "a" * 4 -> "aaaa"
            string_builder.append(letter * freq)

        return "".join(string_builder)


# without shortcut methods:

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count up the occurances.
        counts = collections.Counter(s)

        # Build up the string builder.
        string_builder = []
        sorted_char_freq = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        for char, freq in sorted_char_freq:
            string_builder.append(char * freq)
        
        return ''.join(string_builder)


s = "tree"
obj = Solution()
print(obj.frequencySort(s))


# Complexity Analysis:
# Let n be the length of the input String and k be the number of unique characters in the String.
# We know that k ≤ n, because there can't be more unique characters than there are characters in the String. We 
# also know that k is somewhat bounded by the fact that there's only a finite number of characters in Unicode 
# (or ASCII, which I suspect is all we need to worry about for this question).

# There are two ways of approaching the complexity analysis for this question.
# 1.We can disregard k, and consider that in the worst case, k = n.
# 2.We can consider k, recognising that the number of unique characters is not infinite. This is more accurate for 
#   real world purposes.

# I've provided analysis for both ways of approaching it. I choose not to bring it up for the previous approach, 
# because it made no difference there.

# Time Complexity : O(nlogn) OR O(n + klogk).
# - Putting the characters into the HashMap has a cost of O(n), because each of the n characters must be put in, 
#   and putting each in is an O(1) operation.
# - Sorting the HashMap keys has a cost of O(klogk), because there are k keys, and this is the standard cost for 
#   sorting. If only using n, then it's O(nlogn). For the previous question, the sort was carried out on n items, 
#   not k, so was possibly a lot worse.
# - Traversing over the sorted keys and building the String has a cost of O(n), as n characters must be inserted.
# - Therefore, if we're only considering n, then the final cost is O(nlogn).
# - Considering k as well gives us O(n + klogk), because we don't know which is largest out of n and klogk. 
#   We do, however, know that in total this is less than or equal to O(nlogn).
# Space Complexity : O(n).
# The HashMap uses O(k) space.
# However, the StringBuilder at the end dominates the space complexity, pushing it up to O(n), as every character 
# from the input String must go into it. As said above, it's impossible to do better with the space complexity.
# What's interesting here is that if we only consider n, the time complexity is the same as the previous approach. 
# But by considering k, we can see that the difference is potentially substantial.