import random

from crypto.keygen import keygen
from crypto.encrypt import encrypt
from crypto.decrypt import decrypt

if __name__ == "__main__":
    message = [random.randint(0,1) for _ in range(256)]


    pk, sk = keygen()

    ciphertext = encrypt(pk, message)
    
    plaintext = decrypt(sk, ciphertext)

    print("".join([str(i) for i in message]))
    print("".join([str(i) for i in plaintext]))

    print(plaintext == message)
