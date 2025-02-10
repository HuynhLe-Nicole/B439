import base64

def hamming_distance(str1, str2):
    """Calculate Hamming distance between two byte strings"""
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

def get_blocks(data, size):
    """Split data into blocks of given size"""
    return [data[i:i+size] for i in range(0, len(data), size)]

def find_keysize(ciphertext, min_size=2, max_size=40):
    """Find most likely keysize using Hamming distance"""
    distances = []
    for keysize in range(min_size, max_size + 1):
        blocks = get_blocks(ciphertext, keysize)[:4]  # Take first 4 blocks
        if len(blocks) < 4:  # Skip if not enough blocks
            continue
            
        # Calculate average normalized distance between consecutive blocks
        total_distance = 0
        pairs = 0
        for i in range(len(blocks)-1):
            if len(blocks[i]) == len(blocks[i+1]):  # Only compare equal-length blocks
                distance = hamming_distance(blocks[i], blocks[i+1])
                total_distance += distance / keysize
                pairs += 1
                
        if pairs > 0:
            avg_distance = total_distance / pairs
            distances.append((keysize, avg_distance))
    
    return sorted(distances, key=lambda x: x[1])[:3]  # Return top 3 candidates

def transpose_blocks(ciphertext, keysize):
    """Transpose blocks for single-char XOR analysis"""
    blocks = get_blocks(ciphertext, keysize)
    transposed = []
    
    for i in range(keysize):
        block = bytes(block[i] for block in blocks if i < len(block))
        transposed.append(block)
    
    return transposed

def score_english(text):
    """Score text based on character frequency"""
    # Common English character frequencies
    freq = {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13, 'f': 2.2, 'g': 2.0, 
        'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7,
        'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8,
        'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0, 'z': 0.074, ' ': 13
    }
    
    score = 0
    for char in text.lower():
        if chr(char) in freq:
            score += freq[chr(char)]
    return score

def single_byte_xor(data):
    """Find best single-byte XOR key"""
    best_score = float('-inf')
    best_key = None
    
    for key in range(256):
        decoded = bytes(b ^ key for b in data)
        score = score_english(decoded)
        
        if score > best_score:
            best_score = score
            best_key = key
            
    return best_key

def decrypt_vigenere(ciphertext_b64):
    # Decode base64
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # Find likely key sizes
    key_candidates = find_keysize(ciphertext)
    
    best_result = None
    best_score = float('-inf')
    
    # Try each candidate key size
    for keysize, _ in key_candidates:
        # Split into blocks and transpose
        transposed = transpose_blocks(ciphertext, keysize)
        
        # Find key byte for each position
        key = bytes(single_byte_xor(block) for block in transposed)
        
        # Decrypt with found key
        plaintext = bytes(c ^ key[i % len(key)] for i, c in enumerate(ciphertext))
        
        # Score result
        score = score_english(plaintext)
        if score > best_score:
            best_score = score
            best_result = (key, plaintext)
    
    return best_result

# Test hamming distance
s1 = b"this is a test"
s2 = b"wokka wokka!!!"
assert hamming_distance(s1, s2) == 37, "Hamming distance test failed"

# Main decryption
with open('6.txt') as f:
    ciphertext = f.read().replace('\n', '')
    
key, plaintext = decrypt_vigenere(ciphertext)
print(f"Found key: {key}")
print(f"Plaintext: {plaintext.decode()}")