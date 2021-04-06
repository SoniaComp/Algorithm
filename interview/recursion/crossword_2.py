import itertools


def crosswordPuzzle(crossword, words):
    # preprocess for crossword
    horizontal, vertical = [], []
    for lst in (horizontal, vertical):
        for row in range(10):
            for c, g in itertools.groupby(range(10), key=lambda x: crossword[row][x]):
                l = list(g)
                if c == '-' and len(l) > 1:
                    lst.append([row, l[0], l[-1]])
    crossword = list(map(list, zip(*crossword)))

    # find all intersections
    intersections = [(i, column[0]-row[1], j, row[0]-column[1])
                     for i, row in enumerate(horizontal) for j, column in enumerate(vertical)
                     if row[1] <= column[0] <= row[2] and column[1] <= row[0] <= column[2]]

    words = input().split(';')
    result = None
    for l in itertools.permutations(words, len(words)):
        if all(len(l[i]) == horizontal[i][2] + 1 for i in range(len(horizontal))) and \
            all(len(l[i + len(horizontal)]) == vertical[i][2]-vertical[i][1]+1 for i in range(len(vertical))) and \
                all(l[i[0]][i[1]] == l[i[2] + len(horizontal)][i[3]] for i in intersections):
            result = l
            break

    # fill in the answer
    for i, x in enumerate(horizontal):
        crossword[x[0]][x[1]:x[2]+1] = result[i]
    crossword = list(map(list, zip(*crossword)))
    for i, x in enumerate(vertical):
        crossword[x[0]][x[1]:x[2]+1] = result[i+len(horizontal)]
    crossword = list(map(list, zip(*crossword)))
