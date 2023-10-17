# Decryption
L1_decrypt = L3_encrypt
R1_decrypt = R3_encrypt

f1_decrypt = bitwise_xor(L1_decrypt, K2)
R2_decrypt = bitwise_xor(R1_decrypt, f1_decrypt)
L2_decrypt = L1_decrypt

f2_decrypt = bitwise_xor(L2_decrypt, K1)
L1_final = bitwise_xor(R2_decrypt, f2_decrypt)
R1_final = R2_decrypt

# Retrieve binary plaintext
retrieved_binary_text = L1_final + R1_final

# Convert binary plaintext to integer
retrieved_integer_text = int(retrieved_binary_text, 2)

# Convert the integer to bytes and then to string using binascii.unhexlify()
retrieved_plain_text = binascii.unhexlify('%x' % retrieved_integer_text)

print("Retrieved Plain Text is:", retrieved_plain_text)