import random
import binascii

# Function to generate random binary key of given length
def generate_random_key(length):
    binary_key = ""
    for i in range(length):
        bit = random.randint(0, 1)
        binary_key += str(bit)
    return binary_key

# Function to perform bitwise XOR operation on two binary strings
def bitwise_xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

# Function to convert binary string to decimal
def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

# Plain text input
plain_text = "Hello"
print("Plain Text is:", plain_text)

# Encryption
ascii_values = [ord(char) for char in plain_text]
binary_text = [format(value, '08b') for value in ascii_values]
binary_text = "".join(binary_text)

half_length = len(binary_text) // 2
L1_encrypt = binary_text[:half_length]
R1_encrypt = binary_text[half_length:]

K1 = generate_random_key(len(R1_encrypt))
K2 = generate_random_key(len(R1_encrypt))

f1_encrypt = bitwise_xor(R1_encrypt, K1)
L2_encrypt = bitwise_xor(f1_encrypt, L1_encrypt)
R2_encrypt = R1_encrypt

f2_encrypt = bitwise_xor(L2_encrypt, K2)
L3_encrypt = bitwise_xor(f2_encrypt, R2_encrypt)
R3_encrypt = L2_encrypt

# Ciphertext
cipher_text = L3_encrypt + R3_encrypt
print("Cipher Text:", cipher_text)
