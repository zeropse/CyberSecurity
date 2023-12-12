def substitution_cipher(plain_text, key):
    cipher_text = ""
    
    for char in plain_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift + key) % 26 + shift)
            cipher_text += shifted_char
        else:
            cipher_text += char
    
    return cipher_text

def substitution_decipher(cipher_text, key):
    decrypted_text = ""
    
    for char in cipher_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    
    return decrypted_text

print()
choice = input("Enter 'e' to encrypt and 'd' to decrypt: ").lower()

if choice == "e":
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter key: "))
    cipher_text = substitution_cipher(plain_text, key)
    print("Cipher text:", cipher_text)
elif choice == "d":
    cipher_text = input("Enter the cipher text: ")
    key = int(input("Enter key: "))
    decrypted_text = substitution_decipher(cipher_text, key)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
