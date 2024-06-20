# (x-l/2, y+l/2) = x-h,y+h        (x+l/2, y+l/2) = x+h, y+h
#       |                      |
# (x-l/2, y) = x-h, y ---(x, y)---(x+l/2, y) = x+h, y
#       |                      |
# (x-l/2, y-l/2) = x-h,y-h       (x+l/2, y-l/2) = x+h, y-h
def drawLine(x0, y0, x1, y1):
    print(x0, y0, x1, y1)


def drawHTree(x, y, length, depth):
    if depth == 0:
        return

    h = length / 2

    drawLine(x - h, y + h, x - h, y - h)  # first vertical line
    drawLine(x - h, y, x + h, y)  # horizontal line
    drawLine(x + h, y + h, x + h, y - h)  # second vertical line

    new_length = length / (2 ** 0.5)

    drawHTree(x + h, y + h, new_length, depth - 1)
    drawHTree(x - h, y - h, new_length, depth - 1)
    drawHTree(x - h, y + h, new_length, depth - 1)
    drawHTree(x + h, y - h, new_length, depth - 1)


if __name__ == '__main__':
    solution_input = []
    result = drawHTree(solution_input)
    print(result)
