import os

"""Insert the name of the LeetCode question to create a new folder for the solutions"""


def create_new_folder(new_name):
    current_directory = os.getcwd()

    path = current_directory + '\\' + new_name

    folder_path = os.path.join(current_directory, new_name)

    os.makedirs(folder_path, exist_ok=True)

    return path


def create_python_trivial_solution(path):
    # Specify the file name and path
    file_name = "trivial_solution.py"
    full_path = path + '\\' + file_name

    # Open the file in write mode
    with open(full_path, 'w') as file:
        # Write content to the file
        file.write("# This is a generic file for the trivial solution\n\n")
        file.write("""def solution(solution_input):
    result = []
    return result\n\n\n""")

        file.write("""if __name__ == '__main__':
    solution_input = []
    result = solution(solution_input)
    print(result)""")

        print(f"File '{file_name}' created in {path} successfully.")


def main(leet_code_name):
    new_name = leet_code_name.lower().replace(' ', '-')
    path = create_new_folder(new_name)
    create_python_trivial_solution(path)


if __name__ == '__main__':
    leet_code_name = "total levels in binary tree height"
    main(leet_code_name)




