import re

def main():

    print(count(input("Input: ")))


def count(s):

    # Mencari semua kata "um" dengan regex:
    # - \b: batas kata (word boundary)
    # - \W*: nol atau lebih karakter non-word (untuk menangani tanda baca)
    # - re.IGNORECASE: mengabaikan perbedaan huruf besar/kecil
    um_list = re.findall(r"\b\W*um\b\W*", s, re.IGNORECASE)

    # Inisialisasi counter
    x = 0

    # Jika ditemukan kemunculan "um", update counter
    if len(um_list) != 0:
       x = len(um_list)

    return x

if __name__ == "__main__":
  
    main()
