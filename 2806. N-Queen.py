n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]
print(matrix)

def queen(indices):
    removedIndices = []

    row, col = indices[0], indices[1]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for direction in directions:
        mutiply = 1
        rowDirection, colDirection = direction[0], direction[1]

        while True:
            rowChanged = row + mutiply * rowDirection
            colChanged = col + mutiply * colDirection

            if not checkIndex((rowChanged, colChanged)):
                break
            removedIndices.append((rowChanged, colChanged))

            mutiply += 1

    return removedIndices

    # for i in range(n):
    #     removedRowIndices = (row, i)
    #     removedColIndices = (i, col)
    #
    #     removedIndices.append(removedRowIndices)
    #     removedIndices.append(removedColIndices)
    #
    # if row >= col:
    #     leftDiagonal = (row - col, 0)
    # else:
    #     leftDiagonal = (0, col - row)
    #
    # if row + col <= n:
    #     rightDiagonal = (row + col, 0)
    # else:
    #     rightDiagonal = (row + col + 1 - n, n - 1)



def checkIndex(indices):
    if indices[0] < 0 or indices[0] >= n or indices[1] < 0 or indices[1] >= n:
        return False

    return True