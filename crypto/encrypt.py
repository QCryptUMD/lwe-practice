from maths.error_generation import ErrorGenerator
from maths.polynomial import Polynomial
from maths.linalg import Matrix

import random

MODULUS = 3329
HALF_MODULUS = 3329 // 2

# pk_vector is the vector component of the public key  (As+e)
# pk_matrix is the matrix component of the public key  (A)
# message is an array 256 of 0s and 1s to encrypt
def encrypt(pk, message):
    if len(message) != 256:
        raise ValueError("Only messages of length 256 can be encrypted")

    pk_vector, pk_matrix = pk
    coeffs = [b * HALF_MODULUS for b in message]
    print(coeffs)
    message_poly = Polynomial.from_coefficients(coeffs)
    print(message_poly)

    # generate secret vector r
    # it's okay to use the error vector to generate the secret vector; it's still secure
    r = ErrorGenerator.generate()

    # convert to 3x1 matrix
    r = Matrix([r]).transpose()

    # generate error vector e1 and error scalar e2
    e1 = ErrorGenerator.generate()
    e1 = Matrix([e1]).transpose()
    e2 = ErrorGenerator.generate()[0]


    # These lines maybe work now
    u = pk_matrix.transpose().multiply(r).add(e1)
    v = pk_vector.transpose().multiply(r).matrix[0][0] + e2 + message_poly

    return u, v
