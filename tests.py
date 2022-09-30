import random

from crypto.keygen import keygen
from crypto.encrypt import encrypt

if __name__ == "__main__":
    message = [random.randint(0,1) for _ in range(256)]

    pk, sk = keygen()

    ciphertext = encrypt(pk, message)

    print(ciphertext)
