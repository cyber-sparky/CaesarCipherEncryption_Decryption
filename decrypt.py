# Prompt the user to enter the encrypted password
encrypted_password = input("Enter the encrypted password: ")

# Function to decrypt a character
def decrypt_char(char):
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Shift the character back by 3 positions in the alphabet, wrapping around if necessary
        return chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
    # If the character is not a lowercase letter, leave it unchanged
    return char

# Apply decryption function to each character in the encrypted password using a list comprehension
decrypted_password = ''.join(decrypt_char(char) for char in encrypted_password)

# Print the decrypted password
print("Decrypted password is:", decrypted_password)
