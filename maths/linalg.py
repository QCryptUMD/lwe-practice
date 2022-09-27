class Matrix():
    matrix : list[list[int]]

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

        return sum
        
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
                product[row].append(sum)

        return product
            


# testing

m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[1, 0],[0, 1]])

print(m1.multiply(m2))
print(m1.add(m2))
