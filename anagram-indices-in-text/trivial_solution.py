from collections import Counter
from typing import List


# Time Complexity: O(n*m)
# Space Complexity: O(n+m)
def search(txt: str, pattern: str) -> List[int]:
    pattern_counter = Counter(pattern)
    pattern_length = len(pattern)
    result = []

    for i in range(len(txt)):
        part = txt[i:i + pattern_length]
        part_counter = Counter(part)  # O(m)
        if part_counter == pattern_counter:
            result.append(i)

    return result


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    result = search(haystack, needle)
    print(result)
