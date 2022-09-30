from maths.polynomial import Polynomial
from maths.linalg import Matrix
from maths.error_generation import ErrorGenerator
import random

#Returns a tuple with (public_key, secret_key)
def keygen():
    #Generate the matrix first

    RAND_MAT_SIZE = 3
    MAX_DEGREE = 256

    matA = [ [] for _ in range(RAND_MAT_SIZE) ]

    for row in range(len(matA)):
        for col in range(RAND_MAT_SIZE):

            poly = [ random.randint(0, 1) for _ in range(MAX_DEGREE) ]

            matA[row].append(Polynomial.from_coefficients(poly))

    matA = Matrix(matA)

    # Now generate the secret and error term
    # It's okay to use the error generator for the secret as well

    secret = ErrorGenerator.generate()
    secret = Matrix([secret]).transpose()

    for s in secret.matrix:
        print(s)

    error = ErrorGenerator.generate()
    error = Matrix([error]).transpose()


    public_key = (matA.multiply(secret).add(error), matA)

    return (public_key, secret)

