import copy

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[1][2], matrix[-1][0])
for row in matrix:
    print(row)

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end=" ")
    print()

print([row[0] for row in matrix])                    # first column
print([matrix[i][i] for i in range(3)])              # main diagonal
print([list(col) for col in zip(*matrix)])           # transpose
print([x for row in matrix for x in row])            # flatten
print(sum(sum(row) for row in matrix))

# Ragged (uneven) lists
ragged = [[1], [2, 3], [4, 5, 6]]
print([len(row) for row in ragged])

# Building a grid correctly
bad = [[0] * 3] * 3
bad[0][0] = 5
good = [[0] * 3 for _ in range(3)]
good[0][0] = 5
print(bad)
print(good)

# Copying nested data
m2 = copy.deepcopy(matrix)
m2[0][0] = 100
print(matrix[0][0], m2[0][0])