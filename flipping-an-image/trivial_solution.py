from typing import List


def flip_list(row: List[int]) -> List[int]:
    last_index = len(row) - 1
    for i in range(len(row)):
        if i >= last_index:
            break
        row[i], row[last_index] = row[last_index], row[i]
        last_index -= 1

    return row


def invert_list(row: List[int]) -> List[int]:
    for i, element in enumerate(row):
        match element:
            case 0:
                row[i] = 1
            case 1:
                row[i] = 0
    return row


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    result = []
    for row in image:
        flipped_row = flip_list(row)
        inverted_row = invert_list(flipped_row)
        result.append(inverted_row)
    return result


if __name__ == '__main__':
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    result = flipAndInvertImage(image)
    print(result)
