from copy import deepcopy

import maths.polynomial as poly


class Matrix():
    matrix : list[list[float]]
    #matrix : list[list[poly.Polynomial]]

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        dim1 = (len(self.matrix), len(self.matrix[0]))
        dim2 = (len(other.matrix), len(other.matrix[0]))

        if dim1 != dim2:
            raise Exception("Invalid dimensions")

        sum = [ [] for _ in range(dim1[0])]

        for i in range(dim1[0]):
            for j in range(dim1[1]):
                sum[i].append(self.matrix[i][j] + other.matrix[i][j])
                #sum[i].append(poly.add(self.matrix[i][j] + other.matrix[i][j]))

        return Matrix(sum)

    def multiply(self, other):
        dim1 = (len(self.matrix), len(self.matrix[0]))
        dim2 = (len(other.matrix), len(other.matrix[0]))

        if dim1[1] != dim2[0]:
            raise Exception("Invalid dimensions")

        product = [ [] for _ in range(dim1[0])]
        sum = 0

        for row in range(dim1[0]):
            for col in range(dim2[1]):
                sum = 0.0
                for i in range(0, dim1[1]):
                    sum += self.matrix[row][i] * other.matrix[i][col]
                    #sum = poly.add(sum, poly.multiply(self.matric[row][i], other.matrix[i][col]))
                product[row].append(sum)

        return Matrix(product)

    def transpose(self):
        dim = (len(self.matrix), len(self.matrix[0]))
        t = [ [] for _ in range(dim[1]) ]

        for col in range(dim[1]):
            for row in range(dim[0]):
                t[col].append(deepcopy(self.matrix[row][col]))

        return Matrix(t)

    def scale(self, num):
        dim = (len(self.matrix), len(self.matrix[0]))
        s = [ [] for _ in range(dim[0]) ]

        for row in range(dim[0]):
            for col in range(dim[1]):
                s[row].append(self.matrix[row][col] * num)

        return Matrix(s)


# testing

m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[1, 0],[0, 1]])
m3 = Matrix([[1,2,3],[4,5,6]])

print(m1.multiply(m2).matrix)
print(m1.add(m2).matrix)
print(m3.matrix)
print(m3.transpose().matrix)
print(m1.scale(-23.2).matrix)
