
# Covert hex to base64
import base64

# Define the hex string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Convert hex to raw bytes
raw_bytes = bytes.fromhex(hex_string)

# Encode raw bytes to Base64
base64_string = base64.b64encode(raw_bytes).decode('utf-8')

#Print the result
print(base64_string)