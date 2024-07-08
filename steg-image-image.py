from PIL import Image
import numpy as np

def resize_cover_image(cover_image, target_size):
    resized_cover_image = cover_image.resize(target_size, Image.ANTIALIAS)
    return resized_cover_image

def encode_image_in_image(image_path, cover_image_path, output_path):
    # Load images
    input_image = Image.open(image_path).convert('RGB')
    cover_image = Image.open(cover_image_path).convert('RGB')
    
    if input_image.size != cover_image.size:
        print("Resizing cover image to match input image dimensions.")
        cover_image = resize_cover_image(cover_image, input_image.size)
    
    input_array = np.asarray(input_image)
    cover_array = np.asarray(cover_image)
    
    flat_input = input_array.flatten()
    flat_cover = cover_array.flatten()
    
    # Encode the input image into the cover image
    encoded_flat = np.copy(flat_cover)
    for i in range(len(flat_input)):
        input_pixel = flat_input[i]
        cover_pixel = flat_cover[i]
        
        # Use the most significant 4 bits of the input pixel and the least significant 4 bits of the cover pixel
        encoded_pixel = (cover_pixel & 0b11110000) | (input_pixel >> 4)
        encoded_flat[i] = encoded_pixel
    
    # Convert back to an image
    encoded_array = np.array(encoded_flat, dtype=np.uint8).reshape(input_array.shape)
    encoded_image = Image.fromarray(encoded_array)
    encoded_image.save(output_path)
    print("Encoded Successfully")

def decode_image_in_image(encoded_image_path, output_path):
    encoded_image = Image.open(encoded_image_path).convert('RGB')
    encoded_array = np.asarray(encoded_image)
    
    # Extract the hidden image
    decoded_flat = []
    for pixel in encoded_array.flatten():
        # Extract the least significant 4 bits and shift them back to the original position
        hidden_pixel = (pixel & 0b00001111) << 4
        decoded_flat.append(hidden_pixel)
    
    # Convert back to an image
    decoded_array = np.array(decoded_flat, dtype=np.uint8).reshape(encoded_array.shape)
    decoded_image = Image.fromarray(decoded_array)
    decoded_image.save(output_path)
    print("Decoded Successfully")

# Usage
input_image_path = 'hidden.jpg'  # Replace with the actual path to the hidden image
cover_image_path = 'cover.jpg'   # Replace with the actual path to the cover image
encoded_image_path = 'encoded-image.png'
decoded_image_path = 'decoded-image.png'

encode_image_in_image(input_image_path, cover_image_path, encoded_image_path)
decode_image_in_image(encoded_image_path, decoded_image_path)

'''

from PIL import Image

def encode_image(main_image_path, secret_image_path, output_image_path):
    # Open the main image (where the secret image will be hidden)
    main_image = Image.open(main_image_path).convert('RGB')
    main_pixels = main_image.load()

    # Open the secret image (the image to be hidden)
    secret_image = Image.open(secret_image_path).convert('RGB')
    secret_pixels = secret_image.load()

    width, height = main_image.size

    for y in range(height):
        for x in range(width):
            # Get the RGB values of the main image and secret image
            main_pixel = main_pixels[x, y]
            secret_pixel = secret_pixels[x, y] if x < secret_image.width and y < secret_image.height else (0, 0, 0)
            
            # Encode the secret image into the main image
            new_pixel = (
                (main_pixel[0] & 0xF0) | (secret_pixel[0] >> 4),
                (main_pixel[1] & 0xF0) | (secret_pixel[1] >> 4),
                (main_pixel[2] & 0xF0) | (secret_pixel[2] >> 4)
            )
            
            main_pixels[x, y] = new_pixel

    # Save the encoded image
    main_image.save(output_image_path)
    print(f"Encoded image saved to {output_image_path}")

def decode_image(encoded_image_path, output_image_path, secret_image_size):
    # Open the encoded image
    encoded_image = Image.open(encoded_image_path).convert('RGB')
    encoded_pixels = encoded_image.load()

    secret_image = Image.new('RGB', secret_image_size)
    secret_pixels = secret_image.load()

    width, height = encoded_image.size

    for y in range(height):
        for x in range(width):
            # Get the RGB values of the encoded image
            encoded_pixel = encoded_pixels[x, y]
            
            # Decode the secret image from the encoded image
            secret_pixel = (
                (encoded_pixel[0] & 0x0F) << 4,
                (encoded_pixel[1] & 0x0F) << 4,
                (encoded_pixel[2] & 0x0F) << 4
            )
            
            if x < secret_image.width and y < secret_image.height:
                secret_pixels[x, y] = secret_pixel

    # Save the decoded image
    secret_image.save(output_image_path)
    print(f"Decoded image saved to {output_image_path}")

# Usage
main_image_path = 'cover.jpg'
secret_image_path = 'hidden.jpg'
encoded_image_path = 'encoded_image.png'
decoded_image_path = 'decoded_image.png'
secret_image_size = (200, 200)  # Specify the size of the secret image

# Encode the secret image into the main image
encode_image(main_image_path, secret_image_path, encoded_image_path)

# Decode the secret image from the encoded image
decode_image(encoded_image_path, decoded_image_path, secret_image_size)
'''