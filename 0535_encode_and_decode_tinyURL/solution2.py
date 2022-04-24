# Approach #2 Variable-length Encoding

# Algorithm:
# In this case, we make use of variable length encoding to encode the given URLs. For every longURL, we choose a 
# variable codelength for the input URL, which can be any length between 0 and 61. Further, instead of using only 
# numbers as the Base System for encoding the URLs, we make use of a set of integers and alphabets to be used for 
# encoding.


class Codec:
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}
    count = 1
    
    def getString(self):
        c = self.count
        encStr = ""
        while c > 0:
            c -= 1
            encStr += self.chars[c % 62]
            c /= 62
        return encStr
        
        
    def encode(self, longUrl: str) -> str:
        key = self.getString()
        self.dict[key] = longUrl
        self.count += 1
        return "http://tinyurl.com/" + key
        

    def decode(self, shortUrl: str) -> str:
        return self.dict.get(shortUrl.replace("http://tinyurl.com/", ""))
        

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))


# Performance Analysis:
# - The number of URLs that can be encoded is, again, dependent on the range of int, since, the same count will be 
#   generated after overflow of integers.
# - The length of the encoded URLs isn't necessarily short, but is to some extent dependent on the order in which 
#   the incoming longURL's are encountered. For example, the codes generated will have the lengths in the following 
#   order: 1(62 times), 2(62 times) and so on.
# - The performance is quite good, since the same code will be repeated only after the integer overflow limit, 
#   which is quite large.
# - In this case also, the next code generated could be predicted by the use of some calculations.
