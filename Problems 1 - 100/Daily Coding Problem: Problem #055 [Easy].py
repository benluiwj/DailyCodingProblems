# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Implement a URL shortener with the following methods:

#  * shorten(url), which shortens the url into a six-character alphanumeric
#    string, such as zLg6wl.
#  * restore(short), which expands the shortened string into the original url. If
#    no such shortened string exists, return null.

# Hint: What if we enter the same URL twice?

from typing import *
import string
import random

class Codec:
    def __init__(self):
        self.url_to_short = dict()
        self.short_to_url = dict()
        self.alphanumerals = string.ascii_lowercase() + string.ascii_uppercase() + string.digits()
        self.length = len(self.alphanumerals)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_to_short:
            return  self.url_to_short[longUrl]
        
        shortUrl = ""
        for i in range(6):
            shortUrl += self.alphanumerals[random.randint(0, self.length - 1)]
        
        self.url_to_short[longUrl] = shortUrl
        self.short_to_url[shortUrl] = longUrl
        
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.short_to_url:
            return None
        
        return self.short_to_url[shortUrl]