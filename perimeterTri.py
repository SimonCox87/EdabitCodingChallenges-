"""Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
Examples

perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28

Notes

    The given points always create a triangle.
    The numbers in the argument array can be positive or negative.
    Output should have 2 decimal places
    This challenge is easier than it looks."""
"""def perimeter(lst):
    ab = round(((lst[1][0] - lst[0][0]) ** 2 + (lst[1][1] - lst[0][1]) ** 2) ** 0.5, 2)
    bc = round(((lst[2][0] - lst[1][0]) ** 2 + (lst[2][1] - lst[1][1]) ** 2) ** 0.5, 2)
    cA = round(((lst[0][0] - lst[2][0]) ** 2 + (lst[0][1] - lst[2][1]) ** 2) ** 0.5, 2)
    return round(sum(list((ab, bc, cA))), 2)

print(perimeter([[15, 7], [5, 22], [11, 1]]))
print(perimeter([[0, 0], [0, 1], [1, 0]]))
print(perimeter([[-10, -10], [10, 10 ], [-10, 10]]))"""

def perimeter(lst):
    x, y = zip(*lst)
    aB = ((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) ** 0.5
    bC = ((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2) ** 0.5
    cA = ((x[0] - x[2]) ** 2 + (y[0] - y[2]) ** 2) ** 0.5
    return round(aB + bC + cA, 2)

print(perimeter([[15, 7], [5, 22], [11, 1]]))
print(perimeter([[0, 0], [0, 1], [1, 0]]))
print(perimeter([[-10, -10], [10, 10 ], [-10, 10]]))

"""def perimeter(lst):
	A, B, C = lst
	d = lambda p, q: ((q[0]-p[0])**2 + (q[1]-p[1])**2)**0.5
	return round(d(A, B) + d(B, C) + d(A, C), 2)"""

"""def perimeter(lst):
	return round(sum([((lst[i][0]-lst[i-1][0])**2 + (lst[i][1]-lst[i-1][1])**2)**0.5 for i in range(len(lst))]),2)"""