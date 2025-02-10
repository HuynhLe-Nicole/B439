# from collections import Counter
# import urllib.request

# # Function  to XOR a single byte key with a given ciphertext (in hex format)
# def xor_single_byte(hex_string, key):
#     # Convert hex string to raw bytes
#     ciphertext = bytes.fromhex(hex_string)

#     # XOR each byte with the key
#     return bytes(byte ^ key for byte in ciphertext)


# # Function to score a plaintext  based on how "English-like" it is
# def score_plaintext(plaintext):
#     # Define  a set of common English letters (including space)\
#     common_chars = "etaoinshrdlu ETAOINSHRDLU"  #
#     score = 0
#     for char in plaintext:
#         if chr(char) in common_chars:
#             score += 1
#         elif not chr(char).isprintable():  # Penalize non-printable characters
#             score -= 10
    
#     return score

# # Function to break single-byte XOR encryption by brute-forcing all possible keys (0-255)
# def break_single_byte_xor(hex_string):
#     best_score = -float('inf')  # Initialize the best score to negative infinity
#     best_key = None 
#     best_plaintext = None

#     # Try all possible keys (0-255)
#     for key in range (256):
#         # Decrypt using the current key
#         candidate = xor_single_byte(hex_string, key)

#         # Score the candidate plaintext
#         candidate_score = score_plaintext(candidate)

#         # Keep track of the best result
#         if candidate_score > best_score:
#             best_score = candidate_score
#             best_key = key
#             best_plaintext = candidate.decode('utf-8', errors='ignore')  # Decode the plaintext from bytes to string

#     return best_score, best_key, best_plaintext

# # Download the file using urllib
# file_url = "https://cryptopals.com/static/challenge-data/4.txt"
# response = urllib.request.urlopen(file_url)
# file_content = response.read().decode('utf-8')  # Read and decode the content


# best_overall_score = -float('inf')  # Initialize overall best score to negative infinity
# best_line = None # Store the best line (hex_string) that produced the highest score
# best_key = None # Store the best key found across all lines
# best_plaintext = None # Store the best plaintext found across all lines


# # Split the content into lines
# lines = file_content.splitlines()

# for line in lines:  # Read each line in the file
#     line = line.strip()  # Remove any whitespace or newline characters
#     if line:  # Skip empty lines 
#         # Attempt to decrypt ans score the current line
#         score, key, plaintext = break_single_byte_xor(line)  # Call the function to break XOR for this line

#         # If this line'score is better than the previous best. update the best value 
#         if score >  best_overall_score:
#             best_overall_score = score
#             best_line = line 
#             best_key = key
#             best_plaintext = plaintext

# # Print the result
# print(f"Best Line (Hex): {best_line}")
# print(f"Key: {best_key} (ASCII: {chr(best_key)})")
# print(f"Plaintext: {best_plaintext}")
from collections import Counter
import urllib.request  # Import the requests library to handle HTTP requests

# Function to XOR a single byte key with a given ciphertext (in hex format)
def xor_single_byte(hex_string, key):
    # Convert hex string to raw bytes
    ciphertext = bytes.fromhex(hex_string)  # Converts the input hex string into raw bytes
    # XOR each byte with the key
    return bytes(byte ^ key for byte in ciphertext)  # XORs each byte in the ciphertext with the given key

# Function to score a plaintext based on how "English-like" it is
def score_plaintext(plaintext):
    # Define a set of common English letters (including space)
    common_chars = "etaoinshrdlu ETAOINSHRDLU"  # Common English characters (lowercase and uppercase)
    score = 0  # Initialize score to 0
    for char in plaintext:
        if chr(char) in common_chars:  # If the character is in the common_chars list, increase the score
            score += 1
        elif not chr(char).isprintable():  # Penalize non-printable characters by decreasing the score
            score -= 10
    return score  # Return the final score

# Function to break single-byte XOR encryption by brute-forcing all possible keys (0-255)
def break_single_byte_xor(hex_string):
    best_score = -float('inf')  # Initialize the best score as negative infinity
    best_key = None  # Variable to store the best key
    best_plaintext = None  # Variable to store the best plaintext
    # Try all possible keys (0-255)
    for key in range(256):  # Loop through all possible single-byte keys (0-255)
        # Decrypt using the current key
        candidate = xor_single_byte(hex_string, key)  # Decrypt the ciphertext using the current key
        # Score the candidate plaintext
        candidate_score = score_plaintext(candidate)  # Score the decrypted text based on how "English-like" it is
        # Keep track of the best result
        if candidate_score > best_score:  # If the current score is better than the best score so far
            best_score = candidate_score  # Update the best score
            best_key = key  # Update the best key
            best_plaintext = candidate.decode('utf-8', errors='ignore')  # Decode the plaintext from bytes to string
    # Return the best score, key, and plaintext
    return best_score, best_key, best_plaintext

# Download the file from the URL
file_url = "https://cryptopals.com/static/challenge-data/4.txt"
response = urllib.request.urlopen(file_url)
file_content = response.read().decode('utf-8')

# Process the downloaded content line by line
best_overall_score = -float('inf')  # Initialize overall best score to negative infinity
best_line = None  # Store the best line (hex_string) that produced the highest score
best_key = None  # Store the best key found across all lines
best_plaintext = None  # Store the best plaintext found across all lines

# Split the content into lines
lines = file_content.splitlines()

for line in lines:  # Read each line in the file
    line = line.strip()  # Remove any whitespace or newline characters
    if line:  # Skip empty lines
        # Attempt to decrypt and score the current line
        score, key, plaintext = break_single_byte_xor(line)  # Call the function to break XOR for this line
        # If this line's score is better than the previous best, update the best values
        if score > best_overall_score:
            best_overall_score = score
            best_line = line
            best_key = key
            best_plaintext = plaintext

# Print the result
print(f"Best Line (Hex): {best_line}")  # Print the hex string of the best line
print(f"Key: {best_key} (ASCII: {chr(best_key)})")  # Print the key in both decimal and ASCII form
print(f"Plaintext: {best_plaintext}")  # Print the decrypted plaintext