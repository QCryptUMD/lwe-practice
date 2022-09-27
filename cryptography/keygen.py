# TODO

import random

arr=[]
rows, cols=3,3
for i in range(rows):
    col = []
    for j in range(cols):

        polynomials = [random.randint(0,255)]

        for x in range(0, len(polynomials) - 1):
            polynomials[x] = random.randint(0,1)
        col.append(polynomials)
    arr.append(col)
print(arr)

