import random

bot = ('batu', 'gunting', 'kertas')

while True:
    x = random.choice(bot)
    y = input("Masukkan pilihan (Batu/Gunting/Kertas): ").lower()
    if x == y:
        print(f'bot : {x}')
        print("Seri!")
    elif (x == 'batu' and y == 'gunting') or (x == 'gunting' and y == 'kertas') or (x == 'kertas' and y == 'batu'):
        print(f'bot : {x}')
        print("Kamu kalah!")
    elif (x == 'batu' and y == 'kertas') or (x == 'gunting' and y == 'batu') or (x == 'kertas' and y == 'gunting'):
        print(f'bot : {x}')
        print("Kamu menang!")
    user_input = input("Tekan 'q' untuk keluar atau tekan Enter untuk lanjut: ").lower()
    if user_input == 'q':
        print("Terima kasih telah bermain!")
        break
