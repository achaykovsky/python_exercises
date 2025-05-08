from collections import defaultdict


class Codec:
    def __init__(self):
        self.encoding_dict = defaultdict(str)
        self.decoding_dict = defaultdict(str)
        self.base = "http://tinyurl.com/"

    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encoding_dict:
            # create the encoding. adding a new encoding is making our dictionary larger by one
            hashed = len(self.encoding_dict) + 1
            short_url = self.base + str(hashed)

            # update the dicts as well for future retrieval
            self.decoding_dict[short_url] = longUrl
            self.encoding_dict[longUrl] = short_url
            return self.encoding_dict[longUrl]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoding_dict[shortUrl]


if __name__ == '__main__':
    obj = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    tiny = obj.encode(url)
    print(tiny)
    ans = obj.decode(tiny)
    print(ans)
