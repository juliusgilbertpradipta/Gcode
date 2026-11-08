import random  # Mengimpor modul random 

def main():
    # Meminta pengguna untuk menentukan level permainan
    while True:
        try:
            level = int(input("Level: "))  # Meminta input level dari pengguna
        except ValueError:  # Menangani kesalahan jika input bukan angka
            continue  # Jika terjadi kesalahan, ulangi permintaan input
        if level <= 0:  # Memastikan level positif
            continue  # Jika level tidak valid, ulangi permintaan input

        # Menghasilkan angka acak antara 1 dan level
        num = random.randint(1, level)
        break  # Keluar dari loop setelah mendapatkan level yang valid

    # Meminta pengguna untuk menebak angka
    while True:
        try:
            guess = int(input("Guess: "))  # Meminta input tebakan dari pengguna
            if guess <= 0:  # Memastikan tebakan positif
                continue  # Jika tebakan tidak valid, ulangi permintaan input
        except ValueError:  # Menangani kesalahan jika input bukan angka
            continue  # Jika terjadi kesalahan, ulangi permintaan input

        # Membandingkan tebakan dengan angka yang dihasilkan
        if guess < num:
            print("Too small!")  # Jika tebakan terlalu kecil
        elif guess > num:
            print("Too large!")  # Jika tebakan terlalu besar
        else:
            print("Just right!")  # Jika tebakan benar
            break  # Keluar dari loop jika tebakan benar

if __name__ == "__main__":
    main()  # Menjalankan fungsi main jika file ini dieksekusi
