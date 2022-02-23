# Approach 1: Non-ASCII Delimiter

# Intuition:
# Naive solution here is to join strings using delimiters.
# What to use as a delimiter? 
# - Each string may contain any possible characters out of 256 valid ascii characters.
# So, we have to use non-ASCII unichar character, for example unichr(257) in Python

class Codec:
    def encode(self, strs) -> str:
        # if len(strs) == 0: 
        #     return unichr(258)
        
        return chr(257).join(x for x in strs)
        

    def decode(self, s: str):
        # if s == chr(258): 
        #     return []
        return s.split(chr(257))
        



strs = ["Hello","World"]
codec = Codec()
print("encoded:", codec.encode(strs))
print(codec.decode(codec.encode(strs)))


# Complexity Analysis:
# Time complexity : O(N) both for encode and decode, where N is a number of strings in the input array.
# Space complexity : O(1) for encode to keep the output, since the output is one string. O(N) for decode keep the 
# output, since the output is an array of strings.
