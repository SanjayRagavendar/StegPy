from PIL import Image
import numpy as np

def encode_text(text,encoding='UTF-8',errors='surrogatepass'):
    bits=bin(int.from_bytes(text.encode(encoding,errors),'big'))[2:]
    return bits.zfill(8*(len(bits)+7)//8)

def decode_text(bits,encoding='UTF-8',errors='surrogatepass'):
    integer_value=int(bits,2)
    return integer_value.to_bytes((integer_value.bit_length()+7)//8,'big').decode(encoding=encoding,errors=errors)

def encode_text_in_image(text,image_path,output_path):
    # Converting the image into a one dimensional array
    input_image=Image.open(image_path,'r').convert('RGB')
    image_shape=np.asarray(input_image).shape
    flat_array=np.asarray(input_image).flatten()
    
    #Encoding the text
    encoded_text=encode_text(text)+ '11011011111011110110'

    index=0
    for bit in encoded_text:
        flat_array[index]=flat_array[index] & 0b11111110 | int(bit)
        index+=1
    
    encoded_image=np.array(flat_array).reshape(image_shape)
    encoded_image=Image.fromarray(np.uint8(encoded_image)).convert('RGB')
    encoded_image.save(output_path)

    print("Encrypted Successfully at: ",output_path)

def decode_text_from_image(image_path):
    binary_data=""
    encoded_image=Image.open(image_path,'r').convert('RGB')
    # Converting the image into a one dimensional array
    encoded_image=np.asarray(encoded_image).flatten()
    for i in encoded_image:
        binary_data+=str(i & 0b00000001)
    binary_data=binary_data.split('11011011111011110110')[0]
    print("Decoded Text: ",decode_text(binary_data))


#encode_text_in_image("hello world","demo-image.png","encoded-image.png")

#decode_text_from_image("encoded-image.png")