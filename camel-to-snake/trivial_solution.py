from typing import List


# Time Complexity: O(n*(m^2))
# Space Complexity: O(n*m)
def camel_to_snake(my_list: List[str]) -> List[str]:
    # CamelToSnake
    # camel_to_snake

    # MyID -> my_i_d

    res = []

    for variable_name in my_list:
        converted_var = convert_camel_to_snake(variable_name)
        res.append(converted_var)

    return res


# O(m^2)
def convert_camel_to_snake(variable_name: str) -> str:
    result = variable_name[0].lower()

    for c in range(1, len(variable_name)):
        if 'a' <= variable_name[c] <= 'z':  # variable[c].islower()
            result += variable_name[c]
        else:
            result += '_' + variable_name[c].lower()

    return result


if __name__ == '__main__':
    solution_input = ['CamelToSnake', 'MyID']
    result = camel_to_snake(solution_input)
    print(result)
