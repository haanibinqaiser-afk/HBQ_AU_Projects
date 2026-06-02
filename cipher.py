import sys

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    mode = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])
    print(caesar_cipher(text, shift, mode))