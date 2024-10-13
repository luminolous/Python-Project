def vigenere_cipher(message, mode):
    result = [] # Result digunakan sebagai tempat meletakkan karakter karakter yang telah di enkripsi/dekripsi, karakter-karakter tersebut digabungkan menggunakan fungsi .append()
    key_index = 0
    for char in message: # Memakai enumerate supaya variable message dapat dikeluarkan nilai masing masing dari iterable dan indexnya
        if char.isalpha(): # memakai .isalpha() untuk mengecek apakah karakter tersebut merupakan huruf
            ascii_A = 65 if message.isupper() else 97
            key = 'PFP' if message.isupper() else 'pfp' #key berupa konteks dari pesan yang akan dicari, contoh : TIKTOKACCOUNT
            shift = ord(key[key_index % len(key)]) - ascii_A # Menghitung nilai shift yang akan menentukan seberapa banyak karakter tersebut berpindah
            # Enkripsi dan dekripsi
            if mode == 0:  # Enkripsi
                new_char = chr((ord(char) - ascii_A + shift) % 26 + ascii_A)
            else:  # Dekripsi
                new_char = chr((ord(char) - ascii_A - shift + 26) % 26 + ascii_A)
            result.append(new_char)
            key_index += 1    
        else: # apabila karakter bukan huruf, maka nilai char adalah karakter itu sendiri
            result.append(char) # .append() digunakan untuk menggabungkan karakter yang telah di enkripsi/dekripsi kedalam result dalam bentuk list 
    return ''.join(result) # ''.join(result) digunakan untuk menggabungkan karakter-karakter dalam list/tuple sehingga berbentuk string

# Inputan
T = int(input())
for i in range(T):
    mode = int(input())
    message = input()
    # Ciphertext atau Plaintext yang telah diperoleh di print
    print(f'{vigenere_cipher(message, mode)}') if mode == 0 or mode == 1 else print('Gunakan 0 untuk enkripsi atau 1 untuk dekripsi')
