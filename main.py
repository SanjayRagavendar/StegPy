import colorama
from colorama import Fore, Style
from Steg_Files.steg_image import encode_text_in_image, decode_text_from_image
from Steg_Files.steg_audio import encode_text_in_audio_wav,decode_text_in_audio_wav
from Steg_Files.steg_video import *
from Steg_Files.steg_image_image import encode_image_in_image, decode_image_from_image  
from Steg_Files.steg_text_text import encode_text_in_text, decode_text_from_text


colorama.init()

def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))


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
    1. Text in Image Steganography
    2. Text in Audio Steganography
    3. Text in Video Steganography
    4. Text in Text Steganography
    5. Image in Image Steganography
    
    
Enter The Type of Steganography: """ + Style.RESET_ALL,end="")
    choice = int(input())

    if choice == 1:
        print(Fore.GREEN + Style.BRIGHT + """
              

    Image Steganography:
        1. Hide Text in Image
        2. Extract Text from Image
    Enter The Option: """ + Style.RESET_ALL,end='')
        option = int(input())

        if option == 1:
            image_path = input("Enter the image path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            encode_text_in_image(image_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the image." + Style.RESET_ALL)
        
        elif option == 2:
            image_path = input("Enter the image path: ")
            text = decode_text_from_image(image_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            print(Fore.YELLOW + "Extracted text from the image: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)

    elif choice == 2:
        print(Fore.GREEN + Style.BRIGHT + """
              

    Audio Steganography:
        1. Hide Text in Audio
        2. Extract Text from Audio
    Enter The Option: """ + Style.RESET_ALL,end='')
        option = int(input())

        if option == 1:
            audio_path = input("Enter the audio path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            encode_text_in_audio_wav(audio_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the audio." + Style.RESET_ALL)

        elif option == 2:
            audio_path = input("Enter the audio path: ")
            text = decode_text_in_audio_wav(audio_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            print(Fore.YELLOW + "Extracted text from the audio: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)

    elif choice == 3:
        print(Fore.GREEN + Style.BRIGHT + """
              

    Video Steganography:
        1. Hide Text in Video
        2. Extract Text from Video
    Enter The Option: """ + Style.RESET_ALL,end='')
        option = int(input())

        if option == 1:
            video_path = input("Enter the video path: ")
            text = input("Enter the text to hide: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            hide_text_in_video(video_path, text)
            print(Fore.YELLOW + "Text hidden successfully in the video." + Style.RESET_ALL)
        elif option == 2:
            video_path = input("Enter the video path: ")
            text = extract_text_from_video(video_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            print(Fore.YELLOW + "Extracted text from the video: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)
    
    elif choice == 4:
        print(Fore.GREEN + Style.BRIGHT + """
    
    
    Text Steganography:
        1. Encode Text in Text
        2. Decode Text from Text
    Enter The Option: """ + Style.RESET_ALL,end='')
        option = int(input())

        if option == 1:
            text = input("Enter the text to hide: ")
            path_txt = input("Enter the path of the cover text file: ")
            output_path = input("Enter the path of the output text file: ")
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key,output_path)
            encode_text_in_text(text, path_txt)
            print(Fore.YELLOW + f"Text hidden successfully in the text file: {output_path}" + Style.RESET_ALL)
        
        elif option == 2:
            input_path = input("Enter the path of the text file to decode: ")
            text = decode_text_from_text(input_path)
            key = input("Enter the key (If the key is not required press Enter): ")
            if key != "":
                text = xor_encrypt_decrypt(text, key)
            print(Fore.YELLOW + "Decoded text: " + Style.RESET_ALL, text)
        else:
            print(Fore.RED + "Invalid option selected." + Style.RESET_ALL)

    elif choice == 5:
        print(Fore.GREEN + Style.BRIGHT + """
              
            
    Image in Image Steganography:
        1. Hide Image in Image
        2. Extract Image from Image
    Enter The Option: """ + Style.RESET_ALL,end='')
        option = int(input())

        if option == 1:
            main_image_path = input("Enter the main image path: ")
            secret_image_path = input("Enter the secret image path: ")
            output_image_path = input("Enter the output image path: ")
            encode_image_in_image(main_image_path, secret_image_path, output_image_path)
            print(Fore.YELLOW + "Image hidden successfully in the image." + Style.RESET_ALL)
        
        elif option == 2:
            encoded_image_path = input("Enter the encoded image path: ")
            output_image_path = input("Enter the output image path: ")
            decode_image_from_image(encoded_image_path, output_image_path)
            print(Fore.YELLOW + "Extracted image from the image successfully." + Style.RESET_ALL)

    else:
        print(Fore.RED + "Invalid choice selected." + Style.RESET_ALL)
