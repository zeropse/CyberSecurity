alphabets={
    'a':'m',
    'b':'n',
    'c': 'b',
    'd':'v',
    'e':'c',
    'f':'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ':' ',
    '.':'.',
    ',':',',
    '?':'?',
}
item_list=list(alphabets.values())
key_list=list(alphabets.keys())
def find_key(val):
    pos=item_list.index(val)
    key=key_list[pos]
    return key
def encryption(plain_text):
    cipher_text=''
    for i in plain_text:
        cipher_text+=alphabets[i]
    print(f"The cipher text is {cipher_text}")
def decryption(cipher_text):
    plain_text=''
    for i in cipher_text:
        key=find_key(i)
        plain_text+=key
    print(f"The plain text is {plain_text}")

while True:
    user_input = input("Enter 'e' to do encryption and 'd' to do decryption: ")
    if (user_input == 'e'):
        print()
        words = input("Enter the sentence/word you want to encrypt: ")
        encryption(plain_text=words)

    elif (user_input == 'd'):
        print()
        words = input("Enter the sentence/word you want to decrypt: ")
        decryption(cipher_text=words)

    print()
    repeat = input("Do you want to do again:(y/n) ")
    if repeat == 'n':
        break
    else:
        continue
    