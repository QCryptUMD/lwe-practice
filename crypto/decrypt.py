from maths.linalg import Matrix

MODULUS = 3329
HALF_MODULUS = MODULUS // 2
QUARTER_MODULUS = HALF_MODULUS // 2

def decrypt(secret_key, ciphertext):
    u,v = ciphertext

    message_poly = v - secret_key.transpose().multiply(u).matrix[0][0]

    message = [ (0 if (coeff < QUARTER_MODULUS or coeff > QUARTER_MODULUS + HALF_MODULUS) else 1) 
                for coeff in message_poly.coefficients ]

    return message
