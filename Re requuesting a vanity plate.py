from plates import is_valid  # Mengimpor fungsi is_valid dari modul plates

def test_length():
    assert is_valid("A") == False  # Terlalu pendek, harus False
    assert is_valid("AB") == True   # Panjang valid, harus True
    assert is_valid("ABCDEF") == True  # Panjang valid, harus True
    assert is_valid("ABCDEFG") == False  # Terlalu panjang, harus False

def test_start_letters():
    assert is_valid("CS50") == True  # Valid, dimulai dengan huruf
    assert is_valid("50CS") == False  # Tidak valid, diawali dengan angka
    assert is_valid("1A3B") == False  # Tidak valid, diawali dengan angka
    assert is_valid("5B") == False  # Tidak valid, diawali dengan angka
    assert is_valid("C1") == False  # Tidak valid, huruf diikuti angka

def test_numbers():
    assert is_valid("CS05") == False  # Tidak valid, angka di akhir
    assert is_valid("CS50") == True    # Valid, angka di akhir
    assert is_valid("CS50A") == False  # Tidak valid, angka diikuti huruf

def test_punctuation():
    assert is_valid("CS.50") == False  # Tidak valid, mengandung tanda baca
    assert is_valid("CS 50") == False   # Tidak valid, mengandung spasi
    assert is_valid("CS!50") == False    # Tidak valid, mengandung tanda baca


