import wave
import numpy as np
from pydub import AudioSegment

def encode_text(text,encoding='UTF-8',errors='surrogatepass'):
    bits=bin(int.from_bytes(text.encode(encoding,errors),'big'))[2:]
    return bits.zfill(8*(len(bits)+7)//8)

def decode_text(bits,encoding='UTF-8',errors='surrogatepass'):
    integer_value=int(bits,2)
    return integer_value.to_bytes((integer_value.bit_length()+7)//8).decode(encoding=encoding,errors=errors)


def encode_text_in_audio_wav(text, audio_path, output_path):
    wav_file=wave.open(audio_path,'r')
    input_params=wav_file.getparams()
    print(input_params)
    
    frame=wav_file.readframes(input_params.nframes)
    frame_array = np.frombuffer(frame, dtype=np.uint16 if input_params.sampwidth == 2 else np.uint8).copy()
    wav_file.close()
    print(encode_text(text))
    encoded_text=encode_text(text)+'110110111110111101101101'
    print("Encoded text: ", encoded_text)
    print("Encoded text length: ", len(encoded_text))
    print("Decoded Text:",decode_text(encoded_text[:-24]))
    index=0
    for bit in encoded_text:
        frame_array[index]=frame_array[index] & ~1 | int(bit)
        index+=1
    encoded_frame=''.join(map(str, frame_array[:118]))
    if encoded_frame == encoded_text:
        print("Encoded Successfully")
    else:
        print("Encoding failed")
    print("Encoded Frame array: ",encoded_frame )

    

    output_file=wave.open(output_path,'w')
    output_file.setparams(input_params)
    output_file.writeframes(frame_array.tobytes())
    output_file.close()




def decode_text_in_audio_wav(audio_path):
    wav_file=wave.open(audio_path,'r')
    input_params=wav_file.getparams()
    print(input_params)


    frame=wav_file.readframes(input_params.nframes)
    frame_array = np.frombuffer(frame, dtype=np.uint16 if input_params.sampwidth == 2 else np.uint8).copy()
    wav_file.close()
    binary_data=""
    for i in frame_array:
        binary_data+=str(i & 1)
    print(binary_data[:118-24])
    binary_data=binary_data.split('110110111110111101101101')[0]
    print("Decoded Text: ",decode_text(binary_data))

wav_file=wave.open('demo-audio.wav','r')
n_channels = wav_file.getnchannels()
params=wav_file.getparams()
sample_width = wav_file.getsampwidth()
frame_rate = wav_file.getframerate()
n_frames = wav_file.getnframes()

print("Number of channels: ", n_channels)
print("Sample width: ", sample_width)
print("Frame rate: ", frame_rate)
print("Number of frames: ", n_frames)
print("Params: ", params)

frames=wav_file.readframes(n_frames)
print("Frames: ", frames[:15])
frames_array=np.frombuffer(frames, dtype=np.uint16)
print("Frames array: ", frames_array[:150])

encode_text_in_audio_wav("hello world", "demo-audio.wav", "encoded-audio.wav")
decode_text_in_audio_wav("encoded-audio.wav")




'''
def create_new_filename_with_datetime(original_file_name):
    now = datetime.now()
    formatted_date_time = now.strftime("%Y%m%d_%H%M%S")
    new_file_name = f"{original_file_name.split('.')[0]}_{formatted_date_time}.wav"
    return new_file_name


def encode_text_in_audio_mp3(text, audio_path, output_path):
    input_audio = AudioSegment.from_file(audio_path, format="mp3")
    #print(input_audio.sample_width, input_audio.channels, input_audio.frame_rate)
    #print(input_audio.frame_count())
    #print(input_audio.frame_width)

    raw_data=input_audio.raw_data
    samples=np.frombuffer(raw_data, dtype=np.int16 if input_audio.sample_width == 2 else np.int8).copy()
    print(samples[:10])

    encoded_text=encode_text(text)+'110110111110111101101101'
    print(encoded_text)

    index=0
    for bit in encoded_text:
        samples[index]=samples[index] & ~1 | int(bit)
        index+=1
    
    raw_data=samples.tobytes()
    output_audio=input_audio._spawn(raw_data)
    #output_audio=AudioSegment(data=raw_data, sample_width=input_audio.sample_width, frame_rate=input_audio.frame_rate, channels=input_audio.channels)
    output_audio.export(output_path, format="mp3")

def decode_text_in_audio_mp3(encoded_audio_path):
    input_audio = AudioSegment.from_file(encoded_audio_path, format="mp3")
    raw_data=input_audio.raw_data
    samples=np.frombuffer(raw_data, dtype=np.int16 if input_audio.sample_width == 2 else np.int8).copy()
    binary_data=""
    for i in samples:
        binary_data+=str(i&1)
    print(binary_data[:118])
    binary_data=binary_data.split('110110111110111101101101')[0]
    print("Decoded Text: ",decode_text(binary_data))

encode_text_in_audio_mp3("hello world", "demo-audio-mp3.mp3", "encoded-audio.mp3")
decode_text_in_audio_mp3("encoded-audio.mp3")

def mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_file(mp3_file_path, format="mp3")
    audio.export(wav_file_path, format="wav")
'''