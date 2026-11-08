# Mengimpor modul emoji 
import emoji

def main():
    # Meminta input dari pengguna
    user_input = input("Input (contoh: :smile:, :heart:, dll): ")

    # Mengonversi kode emoji menjadi karakter emoji
    # Menggunakan language='alias'
    emoji_output = emoji.emojize(user_input, language='alias')

    # Menampilkan hasil konversi
    print("Output:", emoji_output)

# Memanggil fungsi main
if __name__ == "__main__":
    main()
