# TODO

from maths.polynomial import Polynomial
from maths.linalg import Matrix
import random

"""
arr=[]
rows, cols=3,3
for i in range(rows):
    col = []
    for j in range(cols):

        rand_val = random.randint(0,255)
        polynomials = []

        for x in range(0, rand_val):
            polynomials.append(random.randint(0,1))
        col.append(Polynomial.from_coefficients(polynomials))
    arr.append(col)
print(arr)
"""

#Generate the matrix first

RAND_MAT_SIZE = 3
MAX_DEGREE = 255
COEFF_MOD = 1

matA = [ [] for _ in range(RAND_MAT_SIZE) ]

for row in range(len(matA)):
    for col in range(RAND_MAT_SIZE):
        degree = random.randint(0, MAX_DEGREE)
        poly = [ random.randint(0, 1) for _ in range(degree + 1) ]

        matA[row].append(Polynomial.from_coefficients(poly))

matA = Matrix(matA)

#print(matA.matrix)

