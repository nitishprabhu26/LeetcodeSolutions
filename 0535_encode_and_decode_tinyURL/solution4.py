# Approach #4 Using random number
# In this case, we generate a random integer to be used as the code. In case the generated code happens to be 
# already mapped to some previous longURL, we generate a new random integer to be used as the code. The data is 
# again stored in a HashMap to help in the decoding process.


import random
import sys


class Codec:
    dict = {}
    key = random.randint(0, sys.maxsize)
        
    def encode(self, longUrl: str) -> str:
        # while self.key in self.dict:
        # OR
        while self.dict.get(self.key):
            self.key = random.randint(0, sys.maxsize)
            
        self.dict[self.key] = longUrl
        return "http://tinyurl.com/" + str(self.key)
        

    def decode(self, shortUrl: str) -> str:
        return self.dict.get(int(shortUrl.replace("http://tinyurl.com/", "")))
                

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))


# Performance Analysis:
# - The number of URLs that can be encoded is limited by the range of int.
# - The average length of the codes generated is independent of the longURL's length, since a random integer is 
#   used.
# - The length of the URL isn't necessarily shorter than the incoming longURL. It is only dependent on the relative 
#   order in which the URLs are encoded.
# - Since a random number is used for coding, again, as in the previous case, the number of collisions could 
#   increase with the increasing number of input strings, leading to performance degradation.
# - Determining the encoded URL isn't possible in this scheme, since we make use of random numbers.
