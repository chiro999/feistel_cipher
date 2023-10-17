import random

# Function to generate random binary key of length p
def generate_random_key(length):
    binary_key = ""
    for i in range(length):
        bit = random.randint(0, 1)
        binary_key += str(bit)
    return binary_key

# Function to perform bitwise XOR operation on two binary strings a and b
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

# Input plain text
plain_text = "Hello"
print("Plain Text:", plain_text)

# Convert plain text to ASCII and then to 8-bit binary format
ascii_values = [ord(char) for char in plain_text]
binary_text = [format(value, '08b') for value in ascii_values]
binary_text = "".join(binary_text)

# Divide the binary text into two halves
half_length = len(binary_text) // 2
left_half = binary_text[:half_length]
right_half = binary_text[half_length:]

# Generate two random keys for the first and second rounds
key1_length = len(right_half)
key2_length = key1_length
key1 = generate_random_key(key1_length)
key2 = generate_random_key(key2_length)

# First round of Feistel network
f1_result = bitwise_xor(right_half, key1)
new_right_half = bitwise_xor(f1_result, left_half)
new_left_half = right_half

# Second round of Feistel network
f2_result = bitwise_xor(new_right_half, key2)
final_right_half = bitwise_xor(f2_result, new_left_half)
final_left_half = new_right_half

# Concatenate the halves to get the binary cipher text
binary_cipher_text = final_left_half + final_right_half

# Convert binary cipher text to string
cipher_text = ''
for i in range(0, len(binary_cipher_text), 7):
    temp_data = binary_cipher_text[i:i + 7]
    decimal_data = binary_to_decimal(temp_data)
    cipher_text += chr(decimal_data)

print("Cipher Text:", cipher_text)