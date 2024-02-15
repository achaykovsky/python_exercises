from typing import List


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    mapping = {"type": 0, "color": 1, "name": 2}
    result = 0
    for curr_list in items:
        if curr_list[mapping[ruleKey]] == ruleValue:
            result += 1
    return result


if __name__ == '__main__':
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    result = countMatches(items, ruleKey, ruleValue)
    print(result)
