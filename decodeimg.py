from PIL import Image
import numpy as np

def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    bits = ''
    for row in data:
        for pixel in row:
            for i in range(3):  # R, G, B
                bits += str(pixel[i] & 1)

    # Split bits into bytes
    all_bytes = [bits[i:i+8] for i in range(0, len(bits), 8)]

    message = ''
    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == '\xFE':  # 11111110 = end marker
            break
        message += char

    print("Hidden message:", message)

# Usage
decode_image("encoded.png")
