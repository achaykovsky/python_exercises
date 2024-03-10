# This is a generic file for the trivial solution

def subtractProductAndSum(n):
    n_str = str(n)
    product, sum = 1, 0
    for digit_str in n_str:
        digit_int = int(digit_str)
        product *= digit_int
        sum += digit_int
    result = product - sum
    return result


if __name__ == '__main__':
    n = 4421
    result = subtractProductAndSum(n)
    print(result)
