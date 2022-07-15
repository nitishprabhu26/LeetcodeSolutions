# Approach : Nick white
# https://youtu.be/k1iowWJimbg
# OR
# https://leetcode.com/problems/find-common-characters/discuss/247558/JavaPython-3-12-liner-and-7-liner-count-and-look-for-minimum./569959

# Algorithm:
# 1. Create a main Frequency Array for 26 Alphabets, initialize it with max value since we need to find characters 
# that are common in every string.
# 2. Iterate through the array of strings and create one more array of frequencies which would store frequencies 
# for individual strings.
# 3. Every time, we update main frequency array with minimum, so that we have an idea what the common elements are.
# 4. Now main array contains all common elements with their frequency values at their respective indices.
# 5. Iterate throgh the main frequency array, append the charecters to result, acoording to their frequencies.


from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charFreqArray = [float('inf')] * 26
        res = []
        
        for string in words:
            charFreqLite = [0] * 26

            for char in string:
                charFreqLite[ord(char) - ord('a')] += 1

            for i in range(26):
                charFreqArray[i] = min(charFreqArray[i], charFreqLite[i])
        
        for index, freq in enumerate(charFreqArray):
            while freq > 0:           
                res.append(chr(index + ord('a')))
                freq -= 1
            
        return res


words = ["bella","label","roller"]
obj = Solution()
print(obj.commonChars(words))


# Complexity Analysis:
# Time complexity: O(Len(A) * (String having max characters)).
# Space Complexity- O(1) since we just created array of 26 Alphabets(lowercase only).