# Approach: Neetcode
# https://youtu.be/B1k_sxOSgv8


class Codec:
    def encode(self, strs) -> str:
        # format: length_of_word + delimiter(#) + string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res



strs = ["Hello","World"]
codec = Codec()
print("encoded:", codec.encode(strs))
print(codec.decode(codec.encode(strs)))


# Complexity Analysis:
# Time complexity : O(N) both for encode and decode, where N is a number of strings in the input array.
# Space complexity : O(1) for encode to keep the output, since the output is one string. O(N) for decode keep the 
# output, since the output is an array of strings.
