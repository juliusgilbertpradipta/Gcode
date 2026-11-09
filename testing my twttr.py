from twttr import shorten  # Mengimpor fungsi shorten dari modul twttr

def test_vowels():

    assert shorten("hey") == "hy"  # Menguji penghilangan 'e'
    assert shorten("Integrated") == "ntgrtd"  # Menguji penghilangan 'I', 'e', 'a', 'e'

def test_punctuation():

    assert shorten("hi, i am joe") == "h,  m j"  # Menguji penghilangan vokal, tanda baca tetap
    assert shorten("a,b,c,d,e,f") == ",b,c,d,,f"  # Menguji penghilangan vokal, koma tetap

def test_numbers():

    assert shorten("zeR0") == "zR0"  # Menguji penghilangan 'e', angka tetap

def main():

    test_vowels()  # Menjalankan test case untuk vokal
    test_punctuation()  # Menjalankan test case untuk tanda baca
    test_numbers()  # Menjalankan test case untuk angka
    print("All tests passed!")  # Menampilkan pesan jika semua test berhasil

if __name__ == "__main__":
    main()  # Menjalankan fungsi main jika file ini dieksekusi
