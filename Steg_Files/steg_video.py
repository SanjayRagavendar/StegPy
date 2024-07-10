import cv2
import numpy as np

def text_to_bin(text):
    """Convert text to a binary string."""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def bin_to_text(binary):
    """Convert a binary string to text."""
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def hide_text_in_frame(frame, text):
    """Hide text in a single frame."""
    binary_text = text_to_bin(text)
    binary_index = 0
    max_len = len(binary_text)
    rows, cols, _ = frame.shape

    for row in range(rows):
        for col in range(cols):
            if binary_index < max_len:
                r, g, b = frame[row, col]
                r = (r & ~1) | int(binary_text[binary_index])  # Modify LSB of red channel
                frame[row, col] = [r, g, b]
                binary_index += 1
            else:
                break
        if binary_index >= max_len:
            break

    return frame

def extract_text_from_frame(frame, text_length):
    """Extract hidden text from a single frame."""
    binary_text = ''
    rows, cols, _ = frame.shape
    binary_index = 0
    max_len = text_length * 8

    for row in range(rows):
        for col in range(cols):
            if binary_index < max_len:
                r, g, b = frame[row, col]
                binary_text += str(r & 1)  # Extract LSB of red channel
                binary_index += 1
            else:
                break
        if binary_index >= max_len:
            break

    return bin_to_text(binary_text)

def hide_text_in_video(input_video_path, output_video_path, text):
    """Hide text in a video."""
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'x264')
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    if not out.isOpened():
        print("Error: Cannot open output video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = hide_text_in_frame(frame, text)
        out.write(frame)

    cap.release()
    out.release()
    print("Text hidden in video successfully.")

def extract_text_from_video(video_path, text_length):
    """Extract hidden text from a video."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return None

    ret, frame = cap.read()
    cap.release()

    if ret:
        return extract_text_from_frame(frame, text_length)
    else:
        print("Error: Cannot read frame from video.")
        return None

# Example usage
"""
input_video = 'cover_video.mp4'
output_video = 'output_with_hidden_text.avi'
secret_text = 'Hello, this is a hidden message!'

# Hide text in video
hide_text_in_video(input_video, output_video, secret_text)

# Extract text from video
extracted_text = extract_text_from_video(output_video, len(secret_text))
print("Extracted Text:", extracted_text)
"""