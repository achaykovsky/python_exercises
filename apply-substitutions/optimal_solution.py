# Time Complexity: O(n)
# Space Complexity: O(n)
def applySubstitutions(replacements: list[list[str]], text: str) -> str:
    mapping = {key: value for key, value in replacements}
    memo = {}

    def resolve(s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if s[i] == '%' and i + 2 < len(s) and s[i + 2] == '%':
                key = s[i + 1]
                if key not in memo:
                    # found an unresolved key
                    memo[key] = resolve(mapping[key])

                result.append(memo[key])
                i += 3  # move 3 steps to skip over %X%
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)

    return resolve(text)


if __name__ == '__main__':
    replacements = [["A", "bce"], ["B", "ace"], ["C", "abc%B%"]]
    text = "%A%_%B%_%C%"
    result = applySubstitutions(replacements, text)
    print(result)
