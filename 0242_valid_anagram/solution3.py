# Approach 2: Frequency List Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_array = [0]*26

        for i in range(len(s)):
            counter_array[ord(s[i]) - ord('a')] += 1
            counter_array[ord(t[i]) - ord('a')] -= 1

        for i in counter_array:
            if i != 0:
                return False
        return True

# OR
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_array = [0]*26

        for i in range(len(s)):
            counter_array[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            counter_array[ord(t[i]) - ord('a')] -= 1
            if counter_array[ord(t[i]) - ord('a')] < 0:
                return False

        return True

# OR
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_array = [0]*26

        for i in range(len(s)):
            counter_array[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            if counter_array[ord(t[i]) - ord('a')] == 0:
                return False
            counter_array[ord(t[i]) - ord('a')] -= 1

        return True
    

s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))


# Complexity analysis:
# Time complexity : O(n). for loop
# Space complexity :  we have 26 charecters in alphabets, it could be considered as O(1) for the list.


# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# Answer:
# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range 
# of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and 
# could adapt to any range of characters.