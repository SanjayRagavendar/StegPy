def text_to_binary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding=encoding, errors=errors), byteorder='big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def binary_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding=encoding, errors=errors)

def encode_text_in_text(message_path, secret_message, output_path):
    with open(message_path, 'r', encoding='utf-8') as file:
        cover_message = file.read()

    binary_data = text_to_binary(secret_message)

    required_length = (len(binary_data) + 1) // 2
    if len(cover_message.replace(" ", "")) < required_length:
        raise ValueError("The original message is not long enough to encode the secret message.")

    zero_width_space = '\u200B'  # Represents binary '00'
    zero_width_non_joiner = '\u200C'  # Represents binary '01'
    zero_width_joiner = '\u200D'  # Represents binary '10'
    word_joiner = '\u2060'  # Represents binary '11'

    encoded_message = ""
    binary_index = 0

    # Split binary data into 2-bit chunks
    while binary_index < len(binary_data):
        if binary_index + 2 <= len(binary_data):
            bits = binary_data[binary_index:binary_index+2]
        else:
            bits = binary_data[binary_index:] + '0'  # Padding to ensure 2 bits

        if bits == '00':
            encoded_message += zero_width_space
        elif bits == '01':
            encoded_message += zero_width_non_joiner
        elif bits == '10':
            encoded_message += zero_width_joiner
        elif bits == '11':
            encoded_message += word_joiner

        binary_index += 2

    full_encoded_message = ""
    message_index = 0
    for char in cover_message:
        full_encoded_message += char
        if message_index < len(encoded_message):
            full_encoded_message += encoded_message[message_index]
            message_index += 1

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(full_encoded_message)

    print("Encoded message saved to:", output_path)

def decode_text_in_text(output_path):
    with open(output_path, 'r', encoding='utf-8') as file:
        encoded_message = file.read()

    zero_width_space = '\u200B'
    zero_width_non_joiner = '\u200C'
    zero_width_joiner = '\u200D'
    word_joiner = '\u2060'

    binary_data = ""
    for char in encoded_message:
        if char == zero_width_space:
            binary_data += '00'
        elif char == zero_width_non_joiner:
            binary_data += '01'
        elif char == zero_width_joiner:
            binary_data += '10'
        elif char == word_joiner:
            binary_data += '11'

    return binary_to_text(binary_data)

# Example usage:
'''
original_message_path = "sample-text.txt"
secret_message = "Super_seCuRe_123"
output_path = "encoded-text.txt"

# Encode the message
encode_message(original_message_path, secret_message, output_path)

print("Original Message Path:", original_message_path)
print("Secret Message:", secret_message)
print("Encoded Message Path:", output_path)

# To decode the message:
decoded_message = decode_message(output_path)
print("Decoded Message:", decoded_message)
'''
