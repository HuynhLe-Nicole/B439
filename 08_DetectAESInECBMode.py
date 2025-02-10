def detect_ecb(ciphertexts):
    # Iterate through each ciphertext
    for i, ciphertext in enumerate(ciphertexts):
        # Split the ciphertext into 16-byte blocks
        blocks = [ciphertext[j:j+16] for j in range(0, len(ciphertext), 16)]
        
        # Check for repeated blocks
        if len(blocks) != len(set(blocks)):
            print(f"ECB-encrypted ciphertext found at line {i + 1}:")
            print(ciphertext.hex())
            return ciphertext

# Step 1: Read the file containing hex-encoded ciphertexts
with open("8.txt", "r") as file:
    ciphertexts = [bytes.fromhex(line.strip()) for line in file]

# Step 2: Detect the ECB-encrypted ciphertext
ecb_ciphertext = detect_ecb(ciphertexts)