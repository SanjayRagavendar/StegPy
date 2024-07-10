import wave
import numpy as np



def encode_text(text, encoding='UTF-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decode_text(bits, encoding='UTF-8', errors='surrogatepass'):
    integer_value = int(bits, 2)
    return integer_value.to_bytes((integer_value.bit_length() + 7) // 8, 'big').decode(encoding, errors)

def encode_text_in_audio_wav(text, audio_path, output_path):
    wav_file = wave.open(audio_path, 'r')
    input_params = wav_file.getparams()
    print(input_params)
    
    frame = wav_file.readframes(input_params.nframes)
    frame_array = np.frombuffer(frame, dtype=np.uint16 if input_params.sampwidth == 2 else np.uint8).copy()
    wav_file.close()

    # Encrypt the text
    encoded_text = encode_text(text) + '110110111110111101101101'  # Append end marker

    print("Encrypted text: ", encoded_text)
    print("Encoded text: ", encoded_text)
    print("Encoded text length: ", len(encoded_text))
    
    index = 0
    for bit in encoded_text:
        frame_array[index] = frame_array[index] & ~1 | int(bit)
        index += 1

    output_file = wave.open(output_path, 'w')
    output_file.setparams(input_params)
    output_file.writeframes(frame_array.tobytes())
    output_file.close()

def decode_text_in_audio_wav(audio_path, key):
    wav_file = wave.open(audio_path, 'r')
    input_params = wav_file.getparams()
    print(input_params)

    frame = wav_file.readframes(input_params.nframes)
    frame_array = np.frombuffer(frame, dtype=np.uint16 if input_params.sampwidth == 2 else np.uint8).copy()
    wav_file.close()

    binary_data = ""
    for i in frame_array:
        binary_data += str(i & 1)
    
    binary_data = binary_data.split('110110111110111101101101')[0]  # Remove end marker
    return encode_text(binary_data)

# Example usage
"""
input_video = 'input.mp4'
output_video = 'output_with_hidden_text.avi'
secret_text = 'Hello, this is a hidden message!'
encryption_key = 'secretkey'

# Hide text in video
encode_text_in_audio_wav(secret_text, 'demo-audio.wav', 'encoded-audio.wav', encryption_key)

# Extract text from video
decode_text_in_audio_wav('encoded-audio.wav', encryption_key)
"""
