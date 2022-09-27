# TODO

from maths.polynomial import Polynomial
import random

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

