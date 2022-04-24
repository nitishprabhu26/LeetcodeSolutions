# Approach #3 Using hashcode

# Algorithm:
# In this method, we make use of an inbuilt function hashCode() to determine a code for mapping every URL. Again, 
# the mapping is stored in a HashMap for decoding.

# The hash code for a String object is computed(using int arithmetic) as −
# s[0]*31^{(n - 1)} + s[1]*31^{(n - 2)} + ... + s[n - 1], where s[i] is the ith character of the string, n is the 
# length of the string.


# https://www.geeksforgeeks.org/python-hash-method/

class Codec:
    dict = {}
        
    def encode(self, longUrl: str) -> str:
        hashedValue = str(hash(longUrl))
        self.dict[hashedValue] = longUrl
        return "http://tinyurl.com/" + hashedValue
        

    def decode(self, shortUrl: str) -> str:
        return self.dict.get(shortUrl.replace("http://tinyurl.com/", ""))
        

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))


# Performance Analysis:
# - The number of URLs that can be encoded is limited by range of int, since hashCode uses integer calculations.
# - The average length of the encoded URL isn't directly related to the incoming longURL length.
# - The hashCode() doesn't generate unique codes for different string. This property of getting the same code for 
#   two different inputs is called collision. Thus, as the number of encoded URLs increases, the probability of 
#   collisions increases, which leads to failure.
# - Thus, it isn't necessary that the collisions start occuring only after a certain number of strings have been 
#   encoded, but they could occur way before the limit is even near to the int. 
#   This is similar to birthday paradox i.e. the probability of two people having the same birthday is nearly 50% 
#   if we consider only 23 people and 99.9% with just 70 people.
# - Predicting the encoded URL isn't easy in this scheme.
