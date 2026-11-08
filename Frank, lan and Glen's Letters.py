import sys  # Mengimpor modul sys 
import random  # Mengimpor modul random
import pyfiglet  # Mengimpor modul pyfiglet

# Membuat objek Figlet
figlet = pyfiglet.Figlet()

# Memeriksa argumen baris perintah
if len(sys.argv) == 1:
    isRandomFont = True  # Jika tidak ada argumen, gunakan font acak
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
    isRandomFont = False  # Jika argumen untuk font diberikan, tidak gunakan font acak
else:
    print("Invalid usage")  # Menampilkan pesan kesalahan
    sys.exit(1)  # Keluar dari program dengan status 1

# Mendapatkan daftar font yang tersedia
font = figlet.getFonts()

if not isRandomFont:
    try:
        # Memeriksa font yang diberikan ada dalam daftar font
        if sys.argv[2] in font:
            figlet.setFont(font=sys.argv[2])  # Mengatur font yang dipilih
        else:
            print("Invalid font name")  # Menampilkan pesan kesalahan
            sys.exit(1)  # Keluar dari program dengan status 1
    except IndexError:
        print("Invalid usage")  # Menangani kesalahan
        sys.exit(1)  # Keluar dari program dengan status 1
else:
    # Memilih font secara acak dari daftar font yang tersedia
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)  # Mengatur font acak yang dipilih

# Meminta input dari pengguna
msg = input("Input: ")

# Menampilkan output dalam bentuk teks
print("Output:")
print(figlet.renderText(msg))
