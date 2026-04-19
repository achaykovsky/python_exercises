from typing import List
from collections import defaultdict


# Time Complexity: O(N * K)
# Space Complexity: O(N * K)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams_dict = defaultdict(list)
    total_list = []

    for word in strs:
        letter_counter = [0] * 26  # frequency of each character a-z
        for char in word:
            letter_counter[ord(char) - ord('a')] += 1  # increment the count for this character

        key = tuple(letter_counter)  # use the frequency tuple as the key
        anagrams_dict[key].append(word)

    for key in anagrams_dict.keys():
        total_list.append(anagrams_dict[key])  # append the grouped anagrams to the result list

    return total_list


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)
