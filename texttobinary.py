def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

# Example usage
input_text = input("Enter text to convert to binary:")
binary_output = text_to_binary(input_text)
print("\nBinary representation:\n" + binary_output)
