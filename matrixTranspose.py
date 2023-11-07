# In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; that is, it switches the row 
# and column indices of the matrix A by producing another matrix, often denoted by A^T.

# Create a function that takes a 2D matrix m and returns a 2D matrix (matrix A^T).
# Examples

# make_transpose([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]) ➞ [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]

# make_transpose([
#   [1, 2],
#   [3, 4],
#   [5, 6]
# ]) ➞ [
#   [1, 3, 5],
#   [2, 4, 6]
# ]

# make_transpose([
#   ["a", "b"]
# ]) ➞ [
#   ["a"],
#   ["b"]
# ]

def make_transpose(m):
    return list(map(list,zip(*m)))

print(make_transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])) # ➞ [[1, 4, 7],[2, 5, 8],[3, 6, 9]]

print(make_transpose([
  [1, 2],
  [3, 4],
  [5, 6]
])) # ➞ [[1, 3, 5],[2, 4, 6]]

print(make_transpose([
  ["a", "b"]
])) # ➞ [["a"],["b"]]

# def make_transpose(m):
#   return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]