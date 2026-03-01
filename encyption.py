import string
import random
def main():
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    print(chars)
    print(key)
    is_running = True
    while is_running:
        x = input("Do you want to encrypt or decrypt? (E/D/Q-Quit): ")
        if x.upper() == 'E':

            text = input("Enter the text to be encrypted: ")
            encrypted_text = ""
            encrypted_char = ""

            #ENCRYPTION

            for char in text:
                index = chars.index(char)
                encrypted_char = key[index]
                encrypted_text += encrypted_char

            print(encrypted_text)
        elif x.upper() == 'D':

            #DECRYPTION

            text = input("Enter the text to be decrypted: ")
            decrypted_char = ""
            decrypted_text = ""
            for char in text:
                index = key.index(char)
                decrypted_char = chars[index]
                decrypted_text += decrypted_char
            print(decrypted_text)
        elif x.upper() == 'Q':
            is_running = False

if __name__ == '__main__':
    main()