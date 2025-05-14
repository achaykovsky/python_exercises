import uuid
import logging


# 1. Generates a random 128-bit UUID4 (universally unique).
# 2. Uses only the first 8 hex characters -> approx. 4 billion combinations.
# 3. Checks if the short URL already exists (collision check).
# 4. If a collision occurs, retries with a new UUID.
# 5. Stores short_url -> long_url mapping.

class Codec:
    def __init__(self):
        self.base = "http://tinyurl.com/"
        self.encoding_dict = {}

    def _generate_token(self, length=8) -> str:
        """Generate a short UUID-based token."""
        return str(uuid.uuid4()).replace("-", "")[:length]

    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL using a UUID4-based token with collision protection."""
        token = self._generate_token()
        short_url = self.base + token

        # Ensure no collision (very unlikely!)
        while short_url in self.encoding_dict:
            token = self._generate_token()
            short_url = self.base + token

        self.encoding_dict[short_url] = longUrl
        return short_url

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def decode(self, shortUrl: str) -> str:
        """Decodes the short URL back to the original long URL."""
        original_url = self.encoding_dict.get(shortUrl, "")
        return original_url


if __name__ == '__main__':
    obj = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    tiny = obj.encode(url)
    print(tiny)
    ans = obj.decode(tiny)
    print(ans)
