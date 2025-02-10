from collections import Counter

def xor_single_byte(hex_string, key):
    #Convert hex string to raw bytes
    ciphertext = bytes.fromhex(hex_string) # Converts the input hex string into raw bytes

    # XOR each bytes with the key
    return bytes( byte ^ key for byte in ciphertext) # XORs each byte in the ciphertext with the given key

def score_plaintext(plaintext):
    # Define a set of common English letters(including space)
    common_chars = "etaoinshrdlu ETAOINSHRDLU" # Common English characters (lowercase and uppercase)

    score = 0  # Initialize score to 0

    for char in plaintext:
        if chr(char) in common_chars: # If the character is in the common_chars list, increase th score
            score += 1
        elif not chr(char).isprintable():  # Penalize non-printable characters by decreasing the score
            score -= 10

    return score  # Return the final score

def break_single_byte_xor(hex_string):
    best_score =  -float('inf')  # Initialize the best score as negative infinity
    best_key = None  # Variable to store the best key
    best_plaintext = None  # Variable to store the best plaintext

    # Try all possible keys (0-255)
    for key in range(256):  # Loop through all possible single-byte keys (0-255)
        # Decrypt using the current key
        candidate =  xor_single_byte(hex_string, key)  # Decrypt the ciphertext using the current key

        # Score the candidate plaintext
        candidate_score = score_plaintext(candidate)  # Score the decrypted text based on how "English-like" it is

        # Keep track of the best result
        if candidate_score > best_score:  # If the current score is better than the best score so far
            best_score = candidate_score  # Update the best score
            best_key = key  # Update the best key
            best_plaintext = candidate  # Update the best plaintext

    # Return the best key and the corresponding plaintext
    return best_key, best_plaintext.decode('utf-8', errors='ignore') # Decode the plaintext from bytes to string

# Input hex string 
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Break the single-byte XOR cipher
key, plaintext = break_single_byte_xor(hex_string)

# Print the results
print(f"Key: {key} (ASCII: {chr(key)})")  # Print the key in  both decimal and ASCII form
print(f"Plaintext: {plaintext}")  # Print the decrypted plaintext