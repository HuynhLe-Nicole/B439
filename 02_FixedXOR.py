# The function that takes two equal-length buffers and produces their XOR combination

def xor_buffers(hex1, hex2):
    # Convert hex strings to raw bytes
    # The 'bytes.fromhex()' method converts a hexadecimal string into its byte representation
    buffer1 = bytes.fromhex(hex1) #Converts the first hex string to bytes
    buffer2 = bytes.fromhex(hex2) #Converts the second hex string to bytes

    # Ensure the buffers are of equal length. 
    # XOR operation can only be performed on buffers of the same length. If they're not equal , we raise an error.
    if len(buffer1) != len(buffer2):
        raise ValueError("Buffer must be of equal length") # Raise an error if lengths don't match
    
    # Perform XOR on corresponding bytes.
    # Using a generator expression inside 'byte()', we iterate over pairs of bytes from both buffers.
    # For each pair of bytes(a, b), we perform XOR using the '^' operator.
    xor_result = bytes(a ^ b for a, b in zip(buffer1, buffer2)) # XORs each pair of bytes

    # Convert the result back to a hex string
    # The '.hex()' method converts the resulting bytes back into a hexadecimal string
    return xor_result.hex()  # Returns the final XOR result as a hex string

# Test the function with the given inputs
hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

#Call the function and print the result
result = xor_buffers(hex1, hex2)
print(result) 