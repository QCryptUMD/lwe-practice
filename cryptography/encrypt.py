import maths.polynomial as poly
import maths.linalg as la

import random

MODULUS = 3329
HALF_MODULUS = 3329 // 2

# pk_vector is the vector component of the public key  (As+e)
# pk_matrix is the matrix component of the public key  (A)
# message is an array 256 of 0s and 1s to encrypt
def encrypt(pk_vector, pk_matrix, message):
    if len(message) != 256:
        raise ValueError("Only messages of length 256 can be encrypted")

    message_poly = poly.Polynomial.from_coefficients([b * HALF_MODULUS for b in message])

    # generate secret vector r
    # it's okay to use the error vector to generate the secret vector; it's still secure
    # r = maths.errorVector()

    # generate error vector e1 and error scalar e2
    # e1 = maths.errorVector()
    # e2 = maths.errorScalar()

    # u = pk_matrix.transpose() * r + e1
    # v = pk_vector.transpose() * r + e2 + message_poly

    # return u, v
