# This is a generic file for the trivial solution

def truncateSentence(s: str, k: int) -> str:
    split_result = s.split(" ")[:k]
    result = " ".join(split_result)
    return result


if __name__ == '__main__':
    s = "Hello how are you Contestant"
    k = 4
    result = truncateSentence(s, k)
    print(result)
