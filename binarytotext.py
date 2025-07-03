"""At 48, numbers appear,
At 65, big letters are near.
At 97, small ones start,
And 32 gives space its part."""
def binary_to_text(binary_input):
    try:
        # Split the binary string into 8-bit chunks
        binary_values = binary_input.strip().split()
        # Convert each binary value to a character
        ascii_characters = [chr(int(b, 2)) for b in binary_values]
        return ''.join(ascii_characters)
    except ValueError:
        return "Invalid binary input. Please use space-separated 8-bit binary numbers."

# Example usage
binary_string = input("Enter binary code (space-separated 8-bit chunks):\n")
word = binary_to_text(binary_string)
print("\nDecoded text:\n" + word)
