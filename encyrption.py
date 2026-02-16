choice = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
if choice == 'E': 
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    encrypted_text = ""
    for char in text:
        text_ascii = ord(char)
        shifted_ascii = text_ascii + shift
        encrypted_char = chr(shifted_ascii)
        encrypted_text += encrypted_char
    print(f"Your encrypted message is:\n{encrypted_text}")
elif choice == 'D':
    text = input("Type your encrypted message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift
    decrypted_text = ""
    for char in text:
        text_ascii = ord(char)
        shifted_ascii = text_ascii - shift
        decrypted_char = chr(shifted_ascii)
        decrypted_text += decrypted_char
    print(f"Your decrypted message is:\n{decrypted_text}")
print("hello world")