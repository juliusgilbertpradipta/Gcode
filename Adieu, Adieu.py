# Mengimpor modul yang diperlukan
import inflect  #penggabungan kata dalam bahasa Inggris
import sys      # Untuk operasi sistem

def main():
    #untuk pengolahan teks
    p = inflect.engine()

    # Daftar untuk menyimpan nama-nama yang dimasukkan
    names = []

    print("Masukkan nama satu per satu. Tekan Ctrl+D (Unix) atau Ctrl+Z (Windows) ketika selesai.")

    # Loop terus menerus untuk mengumpulkan nama
    while True:
        try:
            # Meminta input nama dari pengguna
            name = input("Name: ").strip()  # Menghapus spasi kosong di awal/akhir

            # Validasi: hanya menambahkan nama jika tidak kosong
            if name:
                names.append(name)
            else:
                print("Nama tidak boleh kosong, mohon masukkan nama yang valid.")

        except EOFError:  # Terjadi ketika pengguna menekan Ctrl+D/Ctrl+Z
            print()  # Baris kosong untuk formatting
            break   # Keluar dari loop input

        except KeyboardInterrupt:  # Menangani Ctrl+C
            print("\nInput dihentikan. Membuat pesan perpisahan...")
            break

    # Membuat pesan perpisahan
    if names:  # Hanya lanjut jika ada nama yang dimasukkan
        # Menggabungkan nama dengan konjungsi 'dan' yang benar
        farewell_message = "Adieu, adieu, to " + p.join(names)
        print(farewell_message)
    else:
        print("Tidak ada nama yang dimasukkan. Selamat tinggal!")

if __name__ == "__main__":
    main()
