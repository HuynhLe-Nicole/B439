def repeating_key_xor(plaintext, key):
    # Convert plaintext and key to bytes
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Perform XOR operation
    ciphertext = bytearray()
    for i in range(len(plaintext_bytes)):
        # XOR each byte of plaintext with the corresponding byte of the key
        ciphertext.append(plaintext_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    # Return the result as a hex-encoded string
    return ciphertext.hex()

# Example usage
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

ciphertext = repeating_key_xor(plaintext, key)
print(ciphertext)