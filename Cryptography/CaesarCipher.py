def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 1:  # Encrypt
                new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:  # Decrypt
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

cmd, k = map(int, input().split())
k %= 26  # Menjadikan K tetap diantara 0-25

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break
    
for line in lines:
    print(caesar_cipher(line, k, cmd))
