
def isAnagram(s: str, t: str) -> bool:
    abc_dict_for_s = {key: 0 for key in s}
    abc_dict_for_t = {key: 0 for key in t}

    if len(s) != len(t):
        return False

    for c1, c2 in zip(s, t):
        abc_dict_for_s[c1] += 1
        abc_dict_for_t[c2] += 1

    return abc_dict_for_s == abc_dict_for_t


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    result = isAnagram(s, t)
    print(result)
