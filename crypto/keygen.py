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

    secret = [ [] for _ in range(RAND_MAT_SIZE) ]

    for row in range(len(secret)):
        poly = [ random.randint(0, 1) for _ in range(MAX_DEGREE) ]

        secret.append(Polynomial.from_coefficients(poly))

    secret = Matrix(secret)

    error = ErrorGenerator.generate()

    public_key = (matA.multiply(secret).add(error), matA)

    return (public_key, secret)

#print(matA.matrix)
