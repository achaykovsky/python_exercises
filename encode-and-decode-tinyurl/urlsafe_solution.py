import secrets


# Generate a secure random URL-safe string using secrets.token_urlsafe().
# This secrets.token_urlsafe() function:
# - Uses n bytes of cryptographically secure randomness from the OS.
# - Encodes the bytes using base64 with URL-safe characters (A–Z, a–z, 0–9, '-', '_').
# - Removes any trailing '=' padding.
# Note: The length of the resulting string is longer than n due to base64 encoding.

# secrets.token_urlsafe() is random and that's why it's not one-way! => we need 2 dictionaries.

class Codec:
    def __init__(self):
        self.encoding_dict = {}
        self.decoding_dict = {}
        self.base = "http://tinyurl.com/"
        self.token_length = 6  # can adjust for longer/shorter URLs

    # Time Complexity: O(1)
    # Space Complexity: O(K) - Where K is the number of collisions before generating a unique token.
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.encoding_dict:
            return self.encoding_dict[longUrl]

        while True:
            token = secrets.token_urlsafe(self.token_length)[:self.token_length]
            short_url = self.base + token
            if short_url not in self.decoding_dict:
                break  # ensure no collision

        self.encoding_dict[longUrl] = short_url
        self.decoding_dict[short_url] = longUrl
        return short_url

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.decoding_dict.get(shortUrl, "")


if __name__ == '__main__':
    obj = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    tiny = obj.encode(url)
    print(tiny)
    ans = obj.decode(tiny)
    print(ans)
