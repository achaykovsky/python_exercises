import random


# Time Complexity: O(n), where n is the number of digits (10 in this case)
# Space Complexity: O(n)
def generate_unique_digit_string():
    digits = list("0123456789")
    random.shuffle(digits)
    result = "".join(digits)
    return result


if __name__ == '__main__':
    result = generate_unique_digit_string()
    print(result)
