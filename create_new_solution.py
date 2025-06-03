import logging
import os

"""Insert the name of the LeetCode question to create a new folder for the solutions"""


def create_new_folder(new_name):
    current_directory = os.getcwd()

    path = current_directory + '\\' + new_name

    folder_path = os.path.join(current_directory, new_name)

    os.makedirs(folder_path, exist_ok=True)

    return path


def create_python_trivial_solution(path):
    file_name = "trivial_solution.py"
    full_path = os.path.join(path, file_name)

    if os.path.exists(full_path):
        logging.error(f"File '{file_name}' already exists in: {path}")
        return

    try:
        with open(full_path, 'w') as file:
            file.write("# This is a generic file for the trivial solution\n\n")
            file.write("""def solution(solution_input):
    result = []
    return result\n\n\n""")

            file.write("""if __name__ == '__main__':
    solution_input = []
    result = solution(solution_input)
    print(result)""")

        logging.info(f"File '{file_name}' created in {path} successfully.")
    except Exception as e:
        logging.error(f"Failed to create file '{file_name}' in {path}: {e}")


def main(leet_code_name):
    new_name = leet_code_name.lower().replace(' ', '-')
    path = create_new_folder(new_name)
    create_python_trivial_solution(path)


if __name__ == '__main__':
    leet_code_name = "Unique Paths"
    main(leet_code_name)
