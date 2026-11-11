import re

def main():
    # Meminta pengguna untuk memasukkan alamat IPv4 dan memvalidasinya
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    # Memeriksa format dasar dari alamat IP menggunakan regex
    if re.search(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        list_of_numbers = ip.split(".")
        for number in list_of_numbers:
            # Memeriksa apakah angka berada dalam rentang 0-255
            if int(number) < 0 or int(number) > 255:
                return False
            # Memeriksa apakah ada leading zeros
            if len(number) > 1 and number[0] == '0':
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
