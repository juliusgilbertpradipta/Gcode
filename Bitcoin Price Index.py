import sys  # Mengimpor modul sys
import requests  # Mengimpor modul requests

def main():
   
    # Memeriksa jumlah argumen yang diberikan
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")  # Keluar jika argumen tidak ada

    try:
        # Mengonversi argumen baris perintah menjadi float
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")  # Keluar jika argumen bukan angka

    try:
        # Ganti 'YOUR_API_KEY' dengan API key dari akun CoinCap kamu
        api_key = "8542744e2fcf5c3700fbb4e914864a93a98c1d49c24b7782b5cc44dbfc1042bd"
        url = "https://rest.coincap.io/v3/assets/bitcoin"  # URL untuk mendapatkan data Bitcoin
        headers = {"Authorization": f"Bearer {api_key}"}  # Menyiapkan header dengan API key
        response = requests.get(url, headers=headers)  # Melakukan permintaan GET ke API
        response.raise_for_status()  # Memeriksa apakah permintaan berhasil
        data = response.json()  # Mengonversi respons JSON menjadi dictionary
        price = float(data["data"]["priceUsd"])  # Mengambil harga Bitcoin dalam USD
        total = amount * price  # Menghitung total nilai Bitcoin
        print(f"${total:,.4f}")  # Menampilkan total dengan format mata uang
    except requests.RequestException:
        sys.exit("Request failed")  # Keluar jika permintaan gagal

if __name__ == "__main__":
    main()  # Menjalankan fungsi main jika file ini dieksekusi
