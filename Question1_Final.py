# Encryption function, returns encrypted string
def encrypt_text(raw_text, encrypted_text_filepath, n, m):
    # Put the raw text into a string
    raw_text_string = raw_text.read()
    # Variable for the encrypted string
    encrypted_string = ""
    
    for char in raw_text_string:
        # Check if character is alphabetical
        if char.isalpha():
            # For lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    # Shift forward by n * m (encrypt)
                    new_char = chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
                elif 'n' <= char <= 'z':
                    # Shift backward by n + m (encrypt)
                    new_char = chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
            # For uppercase letters
            elif char.isupper():
                if 'A' <= char <= 'M':
                    # Shift backward by n (encrypt)
                    new_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
                elif 'N' <= char <= 'Z':
                    # Shift forward by m^2 (encrypt)
                    new_char = chr(((ord(char) - ord('A') + m ** 2) % 26) + ord('A'))
        # For all characters that are not alphabetical
        else:
            new_char = char
                
        encrypted_string += new_char
    
    with open(encrypted_text_filepath, "w") as encrypted_file:
        encrypted_file.write(str.format(encrypted_string))
        
    return encrypted_string
        
# Decryption function, returns decrypted string
def decrypt_text(encrypted_text, raw_text_filepath, n, m):
    # Put the encrypted text into a string
    encrypted_text_string = encrypted_text.read()
    # Variable for the decrypted string
    decrypted_string = ""
    
    with open(raw_text_filepath, "r") as raw_text:
        raw_text_string = raw_text.read()
    
    for x, char in enumerate(raw_text_string):
        # Check if character is alphabetical
        if char.isalpha():
            # For lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    # Shift backward by n * m (decrypt)
                    new_char = chr(((ord(encrypted_text_string[x]) - ord('a') - n * m) % 26) + ord('a'))
                elif 'n' <= char <= 'z':
                    # Shift forward by n + m (decrypt)
                    new_char = chr(((ord(encrypted_text_string[x]) - ord('a') + (n + m)) % 26) + ord('a'))
            # For uppercase letters
            elif char.isupper():
                if 'A' <= char <= 'M':
                    # Shift forward by n (decrypt)
                    new_char = chr(((ord(encrypted_text_string[x]) - ord('A') + n) % 26) + ord('A'))
                elif 'N' <= char <= 'Z':
                    # Shift backward by m^2 (decrypt)
                    new_char = chr(((ord(encrypted_text_string[x]) - ord('A') - m ** 2) % 26) + ord('A'))
        # For all characters that are not alphabetical
        else:
            new_char = char
                
        decrypted_string += new_char
    
    return decrypted_string
    
# Function to check if strings match, returns true or false
def check_correctness(raw_text, decrypted_text):
    return raw_text == decrypted_text

def main():
    # File path to the raw text to be encrypted
    raw_text_filepath = "raw_text.txt"
    # File path to where the encrypted text will be saved
    encrypted_text_filepath = "encrypted_text.txt"
    
    # Get user input for n and m
    n = int(input("Enter value of n: "))
    m = int(input("Enter value of m: "))
    # Display output back to the user
    print("You entered", n, "and", m, "\n")
    
    # Encrypt
    print("Encrypting...\n")
    # Open the raw text file and pass it to the encryption function, returns the encrypted text
    with open(raw_text_filepath, "r") as raw_text:
        encrypted_string = encrypt_text(raw_text, encrypted_text_filepath, n, m)
    print("Encryption complete. The encrypted text is stored in", encrypted_text_filepath)
    print("The encrypted text is:")
    print(encrypted_string,"\n")
    
    # Decrypt
    print("Decrypting...\n")
    # Open the encrypted text file and pass it to the decryption function, returns the decrypted text
    with open(encrypted_text_filepath, "r") as encrypted_text:
        decrypted_string = decrypt_text(encrypted_text, raw_text_filepath, n, m)
    print("Decryption complete.")
    print("The decrypted text is:")
    print(decrypted_string,"\n")
        
    # Open the raw text file and compare it to the decrypted text to see if they match
    with open(raw_text_filepath, "r") as raw_text:
        raw_string = raw_text.read()
    # Call the checking function, returns true or false
    is_correct = check_correctness(raw_string, decrypted_string)
    print("Decryption test result:")
    if is_correct:
        print("The decryption is correct. The decrypted text matches the original text.")
    else:
        print("The decryption is incorrect. There is a mismatch between the decrypted and original text.")

# Run the program
if __name__ == "__main__":
    main()