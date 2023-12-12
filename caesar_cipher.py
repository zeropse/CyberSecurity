letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == "d":
        key = -key
    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = (index + key) % num_letters
                result += letters[new_index]
        else:
            result += " "
    return result


print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

print("Do you want to encrypt or decrypt? ")
user_input = input("e / d: ").lower()
print()

if user_input == "e":
    print("*ENCRYPTION MODE SELECTED*")
    print()
    key = int(input("Enter the key (1 to 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f"CIPHER TEXT: {ciphertext}")

elif user_input == "d":
    print("*DECRYPTION MODE SELECTED*")
    print()
    key = int(input("Enter the key (1 to 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f"PLAIN TEXT: {plaintext}")
