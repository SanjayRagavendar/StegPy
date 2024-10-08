# STEGANOGRAPHY PROJECT
A tool for hiding secret information within various forms of media, such as images, audio files, and videos etc.

![ste](https://github.com/user-attachments/assets/37b7539b-bb2e-4dca-84c8-f2177c7727aa)

## Table of Contents:
1.Introduction

2.Features

3.Installation

4.Usage

5.Contributing

6.Architecture

7.License

8.Contact

## Introduction:
This project provides a comprehensive steganography tool that allows users to hide and retrieve secret messages within media files. Steganography is the practice of concealing messages or information within other non-secret text or data, and this project aims to make it easy and secure to perform such operations.
### Text Steganography
Text steganography involves hiding information inside text files.This approach leverages Unicode characters with zero visible width to hide information discreetly within text files. By converting text to binary and embedding it using predefined mappings to zero-width characters, the original cover message is modified subtly to contain the encoded secret message. The decoding process reverses this transformation to retrieve the hidden information. This technique can be useful for steganography purposes, where concealing data within seemingly innocuous content is desirable.
### Image Steganography
This technique utilizes LSB embedding to hide information within the image pixels' least significant bits. It allows for covert communication within digital images while preserving the visual integrity of the image to a large extent. This approach is commonly used in steganography to embed sensitive data discreetly within media files.
### Audio Steganography
This approach allows for hiding textual information within the least significant bits of audio samples in a WAV file, enabling covert communication or data embedding while maintaining the audio's overall integrity and quality. The technique is a form of steganography, where data is concealed within another type of data to avoid detection.
### Video Steganography
This video steganography implementation allows users to hide sensitive text messages within video files, ensuring covert communication. It leverages LSB manipulation to embed and extract data from video frames, maintaining video quality while concealing information. Encryption adds an additional layer of security to the hidden messages. This approach demonstrates a basic form of steganography suitable for educational or experimental purposes.

## Features:
->Hide text messages within image files (JPEG, PNG)

->Retrieve hidden messages from image files

->Support for audio and video steganography (planned)

->Simple and intuitive command-line interface

->High-level security with optional encryption for hidden messages

## Installation:
#### Prerequisites:
```
Python 3.x
Pip (Python package manager)
```
### Steps:

1.Clone the repository
```
https://github.com/SanjayRagavendar/StegPy.git
```
2.Navigate to the project directory
```
cd StegPy
```
3.Install the required dependencies
```
pip install -r requirements.txt
```
### Usage:
#### main.py:
This main file consists the varities of options to choose the encription for differnt medias.
```
python3 main.py
```
```
Type of Steganography:
    1. Text in Image Steganography-steg_image.py
    2. Text in Audio Steganography-steg_audio.py
    3. Text in Video Steganography-steg_video.py
    4. Text in Text Steganography-steg_text_text.py
    5. Image in Image Steganography-steg_image_image.py
```
#### steg_image.py:
This file is used to encode and decode the text in an image.
```
python3 steg_image.py
```
#### steg_image_image.py:
This file is used to encode and decode the image in an image.
```
python3 steg_image_image.py
```
#### steg_video.py:
This file is ude to encode and decode the text ia a video.
```
python3 steg_video.py
```
#### steg_audio.py:
This file is used to encode and decode the text in an audio.
```
python3 steg_audio.py
```
#### steg_text_text.py
This file is used to encode and decode the text in a text.
```
python3 steg_text_text.py
```
### Contributing:
Contributions are welcome! To contribute to this project, follow these steps:
```
1.Fork the repository
2.Create a new branch (git checkout -b feature-branch)
3.Make your changes
4.Commit your changes (git commit -m 'Add some feature')
5.Push to the branch (git push origin feature-branch)
6.Open a pull request
```
Please ensure your code adheres to the project's coding standards and includes appropriate tests.

### Architecture:
![architecture](https://github.com/user-attachments/assets/013ef322-5c0a-437a-bfaf-a7918ff2413c)

### License:
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact:

For questions or support, please reach out:
Email: sanjayragavendar2610@gmail.com | tejus9904@gmail.com | nandhakumar20043@gmail.com | vanithacgu@gmail.com 


