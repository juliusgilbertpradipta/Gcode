import random  # Mengimpor modul random 

def main():

    level = get_level()  # Meminta pengguna untuk memilih level kesulitan
    score = 0  # Inisialisasi skor

    # Mengulangi 10 kali untuk 10 soal penjumlahan
    for _ in range(10):
        x = generate_integer(level)  # Menghasilkan angka acak x
        y = generate_integer(level)  # Menghasilkan angka acak y
        correct = x + y  # Menghitung jawaban yang benar

        # Memberikan 3 kesempatan untuk menjawab
        for attempt in range(3):
            try:
                # Meminta input jawaban dari pengguna
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:  # Memeriksa apakah jawaban benar
                    score += 1  # Menambah skor jika jawaban benar
                    break  # Keluar dari loop jika jawaban benar
                else:
                    print("EEE")  # Menampilkan pesan kesalahan jika jawaban salah
            except ValueError:
                print("EEE")  # Menampilkan pesan kesalahan jika input bukan angka

            # Menampilkan jawaban yang benar setelah 3 kali percobaan
            if attempt == 2:
                print(f"{x} + {y} = {correct}")

    # Menampilkan skor akhir
    print(f"Score: {score}")

def get_level():

    while True:
        try:
            level = int(input("Level: "))  # Meminta input level dari pengguna
            if level in [1, 2, 3]:  # Memeriksa apakah level valid
                return level  # Mengembalikan level yang valid
        except ValueError:
            pass  # Ulangi input jika bukan angka

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)  # Angka acak antara 0 dan 9
    elif level == 2:
        return random.randint(10, 99)  # Angka acak antara 10 dan 99
    else:  # level == 3
        return random.randint(100, 999)  # Angka acak antara 100 dan 999

if __name__ == "__main__":
    main()  # Menjalankan fungsi main jika file ini dieksekusi
