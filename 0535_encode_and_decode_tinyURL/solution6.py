# Approach : Two dictionary approach (one for short and other for long URLs)
# https://youtu.be/qmkVXPJ-9YY


import random

class Codec:
    s = {}
    l = {}
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def encode(self, longUrl: str) -> str:
        while longUrl not in self.l:
            code = "".join([random.choice(self.alphabet) for _ in range(6)])
            if code not in self.s:
                self.s[code] = longUrl
                self.l[longUrl] = code
        return code
        
    def decode(self, shortUrl: str) -> str:
        return self.s[shortUrl]
        

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.decode(codec.encode(url)))
