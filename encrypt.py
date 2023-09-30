# Prompt the user to enter the password
password = input("Enter your password: ")

# Function to encrypt a character
def encrypt_char(char):
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Shift the character by 3 positions in the alphabet, wrapping around if necessary
        return chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    # If the character is not a lowercase letter, leave it unchanged
    return char

# Apply encryption function to each character in the input password using a list comprehension
encrypted_password = ''.join(encrypt_char(char) for char in password)

# Print the encrypted password
print("Encrypted password is:", encrypted_password)
