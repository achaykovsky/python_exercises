import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams_dict = collections.defaultdict(list)
    total_list = []

    for word in strs:
        # creating a key to recognize the words with the same letters
        key = '.'.join(sorted(word))  # sort() function is in-place, so it can't apply on a str which is immutable
        anagrams_dict[key].append(word)

    for key in anagrams_dict.keys():
        total_list.append(anagrams_dict[key])

    return total_list


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)
