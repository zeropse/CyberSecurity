import random

def generate_random_key(length):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))

def cipher(text, key, operation):
    if len(text) != len(key):
        raise ValueError("Text and key must have the same length")
    
    result = ""
    for i in range(len(text)):
        if text[i] == ' ':
            result += ' '
        elif text[i].isalpha():
            text_char = ord(text[i]) - ord('a')
            key_char = ord(key[i]) - ord('a')
            if operation == 'encrypt':
                result_char = (text_char + key_char) % 26
            elif operation == 'decrypt':
                result_char = (text_char - key_char) % 26
            result += chr(result_char + ord('a'))
        else:
            result += text[i]  
    
    return result

while True:
    print()
    user_input = input("Enter 'e' to encrypt and 'd' to decrypt (or 'exit' to quit): ")
    option = user_input.strip().lower()

    if option == 'e':
        plain_text = input("Enter the plaintext: ").strip().lower()
        key = generate_random_key(len(plain_text))
        cipher_text = cipher(plain_text, key, 'encrypt')
        print(f"Cipher Text: {cipher_text}")
        print(f"Key: {key}")
    elif option == 'd':
        cipher_text = input("Enter the ciphertext: ").strip().lower()
        key = input("Enter the key: ").strip().lower()
        plain_text = cipher(cipher_text, key, 'decrypt')
        print(f"Plain Text: {plain_text}")
    elif option == 'exit':
        break
    else:
        print("Invalid option. Please enter 'e', 'd', or 'exit'.")
