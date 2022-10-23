# Remember, Strings are Immutable!
# https://leetcode.com/problems/sort-characters-by-frequency/solution/

# Approach 1: Arrays and Sorting

# Intuition:
# In order to sort the characters by frequency, we firstly need to know how many of each there are. One way to do 
# this is to sort the characters by their numbers so that identical characters are side-by-side (all characters in 
# a programming language are identified by a unique number). Then, knowing how many times each appears will be a 
# lot easier.
# Because Strings are immutable though, we cannot sort the String directly. Therefore, we'll need to start by 
# converting it from a String to an Array of characters. Now that we have an Array, we can sort it, which will 
# make all identical characters side-by-side.
# then continue.
# https://leetcode.com/problems/sort-characters-by-frequency/solution/


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return s
        
        # Convert s to a list.
        s = list(s)
        
        # Sort the characters in s.
        s.sort()
        
        # Make a list of strings, one for each unique char.
        all_strings = []
        cur_sb = [s[0]]
        for c in s[1:]:
            # If the last character on string builder is different...
            if cur_sb[-1] != c:
                all_strings.append("".join(cur_sb))
                cur_sb = []
            cur_sb.append(c)
        all_strings.append("".join(cur_sb))
        
        # Sort the strings by length from *longest* to shortest.
        all_strings.sort(key=lambda string : len(string), reverse=True)
        
        # Convert to a single string to return.
        # Converting a list of strings to a string is often done
        # using this rather strange looking python idiom.
        return "".join(all_strings)


s = "tree"
obj = Solution()
print(obj.frequencySort(s))


# Complexity Analysis:
# Let n be the length of the input String.
# Time Complexity: O(n.logn).
# - The first part of the algorithm, converting the String to a List of characters, has a cost of O(n), because 
#   we are adding n characters to the end of a List.
# - The second part of the algorithm, sorting the List of characters, has a cost of O(n.logn).
# - The third part of the algorithm, grouping the characters into Strings of similar characters, has a cost of O(n) 
#   because each character is being inserted once into a StringBuilder and once converted into a String.
# - Finally, the fourth part of the algorithm, sorting the Strings by length, has a worst case cost of O(n), which 
#   occurs when all the characters in the input String are unique.
# - Because we drop constants and insignificant terms, we get O(n.logn) + 3⋅O(n) = O(n.logn).
# - Be careful with your own implementation—if you didn't do the string building process in a sensible way, then 
#   your solution could potentially be O(n^2).
# Space Complexity: O(n). It is impossible to do better with the space complexity, because Strings are immutable. 
# The List of characters, List of Strings, and the final output String, are all of length n, so we have a space 
# complexity of O(n).