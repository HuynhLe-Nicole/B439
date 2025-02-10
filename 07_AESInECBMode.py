from base64 import b64decode
from Crypto.Cipher import AES

# Step 1: Read the Base64-encoded content from the file
with open("7.txt", "r") as file:
    ciphertext_b64 = file.read()

# Step 2: Decode the Base64 content into raw bytes
ciphertext = b64decode(ciphertext_b64)

# Step 3: Define the key
key = b"YELLOW SUBMARINE"

# Step 4: Initialize AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Step 5: Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext)

# Step 6: Remove padding (PKCS#7)
# PKCS#7 padding adds bytes equal to the padding length at the end of the plaintext
padding_length = plaintext[-1]
plaintext = plaintext[:-padding_length]

# Print the decrypted plaintext
print(plaintext.decode("utf-8"))