from collections import Counter


# Time Complexity: O(n)
# Space Complexity: O(1) - since the alphabet size is fixed (26 lowercase letters)
def firstUniqChar(s: str) -> int:
    result = -1
    letters_dict = Counter(s)  # Count frequency of each character

    for i, c in enumerate(s):
        if letters_dict[c] == 1:  # Check if the character is unique
            return i  # Return the index of the first unique character

    return result


if __name__ == '__main__':
    s = "loveleetcode"
    result = firstUniqChar(s)
    print(result)
