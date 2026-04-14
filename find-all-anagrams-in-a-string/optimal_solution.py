from collections import Counter


# Time Complexity: O(n)
# Space Complexity: O(m) = O(26) = O(1) - size of the Counter dictionaries which are at max the size of the English alphabet

def search(txt: str, pattern: str) -> [int]:
    pattern_length = len(pattern)
    txt_length = len(txt)
    result = []

    if pattern_length > txt_length:
        return result

    window_counter = Counter()  # at most 26

    anagram_counter = Counter(pattern)  # at most 26

    left, right = 0, 0

    while right < txt_length:
        # expanding the window to the right
        window_counter[txt[right]] += 1

        # reached the size of the window
        # validate the anagram existence
        if right - left + 1 == pattern_length:
            if window_counter == anagram_counter:
                result.append(left)  # left is the starting index of the window

            # not an anagram -> remove the left side of the window
            # move the window to find an anagram in the next iteration
            window_counter[txt[left]] -= 1
            left += 1
        right += 1

    return result


if __name__ == '__main__':
    txt = "sadbutsad"
    pattern = "sad"
    result = search(txt, pattern)
    print(result)
