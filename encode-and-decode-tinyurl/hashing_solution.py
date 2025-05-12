import hashlib


# Use SHA-256 to generate a deterministic hash of the long URL.
# - Encode the long URL as bytes and hash it with hashlib.sha256().
# - Convert the hash digest to hex and take the first few characters for the short URL token.
# - This reduces the URL to a fixed-length, mostly unique string.
# - Shorter slices (e.g. 6 chars) increase collision risk, so balance length vs URL size.


# Use SHA-256 to generate a deterministic hash of the long URL.
class Codec:
    def __init__(self):
        self.base = "http://tinyurl.com/"
        self.encoding_dict = {}

    # Time Complexity: O(L), where L is the length of the long URL
    # Space Complexity: O(n*L)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL using SHA-256 hash."""
        # Hash the URL and take the first 6 characters for the short version
        hash_digest = hashlib.sha256(longUrl.encode()).hexdigest()
        token = hash_digest[:6]  # You can increase length to reduce collision risk
        short_url = self.base + token

        self.encoding_dict[short_url] = longUrl
        return short_url

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL using stored mapping."""
        return self.encoding_dict.get(shortUrl, "")


if __name__ == '__main__':
    obj = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    tiny = obj.encode(url)
    print(tiny)
    ans = obj.decode(tiny)
    print(ans)
