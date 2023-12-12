import random
from sympy import mod_inverse, isprime

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    totient = (p - 1) * (q - 1)
    e = choose_public_exponent(totient)
    d = mod_inverse(e, totient)
    return ((n, e), (n, d))

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

def choose_public_exponent(totient):
    e = 65537
    while gcd(e, totient) != 1:
        e += 2
    return e

def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_text)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

bits = 2048
public_key, private_key = generate_keypair(bits)
message = "Hello, RSA! This is a longer code example."
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")