from collections import Counter
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(m)
def search(txt: str, pattern: str) -> List[int]:
    pattern_length = len(pattern)
    txt_length = len(txt)
    result = []

    if pattern_length > txt_length:
        return result

    pattern_counter = Counter(pattern)
    window_counter = Counter(txt[:pattern_length])

    if window_counter == pattern_counter:
        result.append(0)

    for i in range(1, txt_length - pattern_length + 1):
        # Add the next character in the window
        window_counter[txt[i + pattern_length - 1]] += 1

        # Remove the character that is no longer in the window
        window_counter[txt[i - 1]] -= 1

        # Clean up the counter to avoid storing characters with a count of 0
        if window_counter[txt[i - 1]] == 0:
            del window_counter[txt[i - 1]]

        if window_counter == pattern_counter:
            result.append(i)

    return result


if __name__ == '__main__':
    txt = "sadbutsad"
    pattern = "sad"
    result = search(txt, pattern)
    print(result)
