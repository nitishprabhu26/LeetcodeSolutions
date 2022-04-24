# Approach #1 Using Simple Counter
# In order to encode the URL, we make use of a counter(i), which is incremented for every new URL encountered. We 
# put the URL along with its encoded count(i) in a HashMap. This way we can retrieve it later at the time of 
# decoding easily.


class Codec:
    dict = {}
    i = 0
    
    def encode(self, longUrl: str) -> str:
        self.dict[self.i] = longUrl
        self.i += 1
        return "http://tinyurl.com/" + str(self.i - 1)
        

    def decode(self, shortUrl: str) -> str:
        return self.dict.get(int(shortUrl.replace("http://tinyurl.com/", "")))
        

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))


# Performance Analysis:
# - The range of URLs that can be decoded is limited by the range of int.
# - If excessively large number of URLs have to be encoded, after the range of int is exceeded, integer overflow 
#   could lead to overwriting the previous URLs' encodings, leading to the performance degradation.
# - The length of the URL isn't necessarily shorter than the incoming longURL. It is only dependent on the 
#   relative order in which the URLs are encoded.
# - One problem with this method is that it is very easy to predict the next code generated, since the pattern can 
#   be detected by generating a few encoded URLs.
