import string
import random

all_characters = string.ascii_letters + string.digits + string.punctuation + " "
all_characters = list(all_characters)
shuffled_chars = all_characters.copy()
random.shuffle(shuffled_chars)

print("")
print("*********** Welcome to Python Encryption and Decryption Program ***********")
print("")
while True:
    action = input("Choose Your Action (E: Encrypt Text, D: Decrypt Text, Q: Quit Program): ").upper()

    if action == "Q":
        print("")
        print("********************** Thanks for Using this Program **********************")
        break

    elif action == "E":
        decrypted_text = input("Enter Text to Encrypt: ")
        encrypted_text = ""

        for character in decrypted_text:
            index = all_characters.index(character)
            encrypted_text += shuffled_chars[index]

        print(f"Encrypted Text       : {encrypted_text}")
        print("")
        continue

    elif action == "D":
        encrypted_text = input("Enter Text to Decrypt: ")
        decrypted_text = ""

        for character in encrypted_text:
            index = shuffled_chars.index(character)
            decrypted_text += all_characters[index]

        print(f"Decrypted Text       : {decrypted_text}")
        print("")
        continue

    else:
        print("Invalid Selection!")
        print("")
        continue

print("")
