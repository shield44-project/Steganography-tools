from PIL import Image
import numpy as np

def to_bin(data):
    return ''.join(format(ord(char), '08b') for char in data)

def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    binary_message = to_bin(secret_message) + '11111110'  # Add end marker
    message_idx = 0
    total_bits = len(binary_message)

    for row in data:
        for pixel in row:
            for i in range(3):  # R, G, B channels
                if message_idx < total_bits:
                    pixel[i] = int((int(pixel[i]) & ~1) | int(binary_message[message_idx]))
                    message_idx += 1

    if message_idx < total_bits:
        raise ValueError("Message is too long for this image!")

    encoded_img = Image.fromarray(data)
    encoded_img.save(output_path)
    print(f"Message encoded successfully into {output_path}")

# Example usagepixel
# Make sure 'original.png' exists in the same folder
encode_image("shield44.png", "This is a hidden message from shield44 take it : 89504E470D0A1A0A0000000D4948445200000145000001760806000000F99A8A5E0000000473424954080808087C086488000000097048597300000EC400000EC401952B0E1B0000001974455874536F667477617265007777772E696E6B73636170652E6F72679BEE3C1A0000200049444154789CECBD69B4A6595526F89C77", "encoded.png")

