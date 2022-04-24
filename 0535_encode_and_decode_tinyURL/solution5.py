# Approach #5 Random fixed-length encoding
# In this case, again, we make use of the set of numbers and alphabets to generate the coding for the given URLs, 
# similar to Approach 2. But in this case, the length of the code is fixed to 6 only. Further, random characters 
# from the string to form the characters of the code. In case, the code generated collides with some previously 
# generated code, we form a new random code.


import random


class Codec:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}
    key = ""
        
    def getRand(self):
        encStr = ""
        for i in range(0, 6):
            encStr += self.alphabet[random.randint(0,61)]
        return encStr
    
    def encode(self, longUrl: str) -> str:
        self.key = self.getRand()
        while self.key in self.dict:
            self.key = self.getRand()
            
        self.dict[self.key] = longUrl
        return "http://tinyurl.com/" + str(self.key)
        

    def decode(self, shortUrl: str) -> str:
        return self.dict.get(shortUrl.replace("http://tinyurl.com/", ""))
        

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))


# Performance Analysis:
# - The number of URLs that can be encoded is quite large in this case, nearly of the order (10 + 26*2)^6.
# - The length of the encoded URLs is fixed to 6 units, which is a significant reduction for very large URLs.
# - The performance of this scheme is quite good, due to a very less probability of repeated same codes generated.
# - We can increase the number of encodings possible as well, by increasing the length of the encoded strings. 
#   Thus, there exists a tradeoff between the length of the code and the number of encodings possible.
# - Predicting the encoding isn't possible in this scheme since random numbers are used.
