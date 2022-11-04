# Using a temporary array to store vowel_index pair and then reverse it.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_index = []
        
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                vowel_index.append([s[i],i])
                
        vowel_index.reverse()
        
        z = len(vowel_index)-1
        
        # pair up new index values for each vowel in the reverse array
        reverse_array = [[vowel_index[i][0], vowel_index[z - i][1]] for i in range(len(vowel_index))]
        
        s_list = list(s)
        
        for i in reverse_array:
            s_list[i[1]] = i[0]
            
        return "".join(s_list)
        

# same as above, but without reversing 'vowel_index' and storing in the new array

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_index = []
        
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                vowel_index.append([s[i],i])
                
        print(vowel_index)
        
        s_list = list(s)
        z = len(vowel_index)
        
        for i in range(z):
            index = vowel_index[i][1]
            vowel = vowel_index[z - i - 1][0]
            s_list[index] = vowel
            
        return "".join(s_list)


s = "leetcode"
obj = Solution()
print(obj.reverseVowels(s))


# Complexity analysis:
# Time complexity : O(n) for a array of length n.
# Space complexity : O(n).

