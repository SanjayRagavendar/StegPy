from PIL import Image
import wave
import cv2
import colorama
from colorama import Fore, Style

colorama.init()

def xor_with_key(text, key):
    key_length = len(key)
    xor_result = [chr(ord(text[i]) ^ ord(key[i % key_length])) for i in range(len(text))]
    return ''.join(xor_result)

# Image Steganography 
def hide_text_in_image(image_path, text):
    image = Image.open(image_path)
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    max_chars = (image.width * image.height * 3) // 8  # 3 channels (R, G, B)
    if len(binary_text) > max_chars:
        raise ValueError("Text is too long to be hidden in the image.")
    pixels = list(image.getdata())
    new_pixels = []
    text_index = 0
    for pixel in pixels:
        binary_pixel = [format(value, '08b') for value in pixel]
        for i in range(3):  # Modify R, G, B channels
            if text_index < len(binary_text):
                binary_pixel[i] = binary_pixel[i][:-1] + binary_text[text_index]
                text_index += 1
        new_pixel = tuple(int(binary, 2) for binary in binary_pixel)
        new_pixels.append(new_pixel)
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_pixels)
    new_image.save("output.png")

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    binary_text = ""
    pixels = list(image.getdata())
    for pixel in pixels:
        binary_pixel = [format(value, '08b') for value in pixel]
        for i in range(3):  # Extract from R, G, B channels
            binary_text += binary_pixel[i][-1]
    text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        text += chr(int(byte, 2))
    return text

# Audio Steganography
def hide_text_in_audio(audio_path, text):
    audio = wave.open(audio_path, mode='rb')
    frames = audio.readframes(audio.getnframes())
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    max_chars = len(frames) // 8
    if len(binary_text) > max_chars:
        raise ValueError("Text is too long to be hidden in the audio.")
    new_frames = bytearray(frames)
    text_index = 0
    for i in range(0, len(new_frames), 2):
        if text_index < len(binary_text):
            new_frames[i] = (new_frames[i] & 0xFE) | int(binary_text[text_index])
            text_index += 1
    new_audio = wave.open("output.wav", mode='wb')
    new_audio.setparams(audio.getparams())
    new_audio.writeframes(new_frames)
    audio.close()
    new_audio.close()

def extract_text_from_audio(audio_path):
    audio = wave.open(audio_path, mode='rb')
    frames = audio.readframes(audio.getnframes())
    binary_text = ""
    for i in range(0, len(frames), 2):
        binary_text += str(frames[i] & 1)
    text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        text += chr(int(byte, 2))
    audio.close()
    return text

# Video Steganography
def hide_text_in_video(video_path, text):
    video = cv2.VideoCapture(video_path)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    max_chars = (frame_width * frame_height * 3) // 8
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    if len(binary_text) > max_chars:
        raise ValueError("Text is too long to be hidden in the video.")
    output_path = "output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    text_index = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        for i in range(frame_height):
            for j in range(frame_width):
                for k in range(3):  # Modify R, G, B channels
                    if text_index < len(binary_text):
                        frame[i, j, k] = (frame[i, j, k] & 0xFE) | int(binary_text[text_index])
                        text_index += 1
        output_video.write(frame)
    video.release()
    output_video.release()

def extract_text_from_video(video_path):
    video = cv2.VideoCapture(video_path)
    binary_text = ""
    while True:
        ret, frame = video.read()
        if not ret:
            break
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                for k in range(3):  # Extract from R, G, B channels
                    binary_text += str(frame[i, j, k] & 1)
    text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        text += chr(int(byte, 2))
    video.release()
    return text

if __name__=="__main__":
    print(Fore.YELLOW + Style.BRIGHT + """
███████╗████████╗███████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗ ██╗   ██╗
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ████╗  ██║██╔═══██╗██╔══██╗╚██╗ ██╔╝
███████╗   ██║   █████╗  ██║  ███╗██╔██╗ ██║██║   ██║██████╔╝ ╚████╔╝ 
╚════██║   ██║   ██╔══╝  ██║   ██║██║╚██╗██║██║   ██║██╔═══╝   ╚██╔╝  
███████║   ██║   ███████╗╚██████╔╝██║ ╚████║╚██████╔╝██║        ██║   
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝        ╚═╝   
                                                    - by ROOT Squad  
""" + Style.RESET_ALL)

    print(Fore.CYAN + Style.BRIGHT + """
Type of Steganography:
    1. Image Steganography
    2. Audio Steganography
    3. Video Steganography
Enter The Type of Steganography: """ + Style.RESET_ALL)
    choice = int(input())
    if choice == 1:
        print(Fore.GREEN + Style.BRIGHT + """
    Image Steganography:
        1. Hide Text in Image
        2. Extract Text from Image
    Enter The Option: """ + Style.RESET_ALL)
        option = int(input())
        if option == 1:
            image_path = input("Enter the image path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            hide_text_in_image(image_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the image." + Style.RESET_ALL)
        elif option == 2:
            image_path = input("Enter the image path: ")
            text = extract_text_from_image(image_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            print(Fore.YELLOW + "Extracted text from the image: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)
    elif choice == 2:
        print(Fore.GREEN + Style.BRIGHT + """
    Audio Steganography:
        1. Hide Text in Audio
        2. Extract Text from Audio
    Enter The Option: """ + Style.RESET_ALL)
        option = int(input())
        if option == 1:
            audio_path = input("Enter the audio path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            hide_text_in_audio(audio_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the audio." + Style.RESET_ALL)
        elif option == 2:
            audio_path = input("Enter the audio path: ")
            text = extract_text_from_audio(audio_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            print(Fore.YELLOW + "Extracted text from the audio: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)
    elif choice == 3:
        print(Fore.GREEN + Style.BRIGHT + """
    Video Steganography:
        1. Hide Text in Video
        2. Extract Text from Video
    Enter The Option: """ + Style.RESET_ALL)
        option = int(input())
        if option == 1:
            video_path = input("Enter the video path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            hide_text_in_video(video_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the video." + Style.RESET_ALL)
        elif option == 2:
            video_path = input("Enter the video path: ")
            text = extract_text_from_video(video_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_with_key(text, key)
            print(Fore.YELLOW + "Extracted text from the video: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice selected." + Style.RESET_ALL)
