def value(greeting):
    greeting = greeting.strip().lower()  # Menghapus spasi di awal/akhir dan mengubah ke huruf kecil
    if greeting.startswith("hello"):
        return 0  # Mengembalikan 0 jika sapaan dimulai dengan "hello"
    elif greeting.startswith("h"):
        return 20  # Mengembalikan 20 jika sapaan dimulai dengan huruf 'h'
    else:
        return 100  # Mengembalikan 100 untuk sapaan lainnya

from bank import value  # Mengimpor fungsi value dari modul bank

def test_hello():
    assert value("hello") == 0  # Menguji sapaan "hello"
    assert value("Hello there") == 0  # Menguji sapaan "Hello there"
    assert value("  HELLO  ") == 0  # Menguji sapaan "  HELLO  " dengan spasi

def test_h_only():
    assert value("hi") == 20  # Menguji sapaan "hi"
    assert value("hey") == 20  # Menguji sapaan "hey"
    assert value("howdy") == 20  # Menguji sapaan "howdy"

def test_other_greetings():
    assert value("good morning") == 100  # Menguji sapaan "good morning"
    assert value("what's up") == 100  # Menguji sapaan "what's up"
    assert value("yo") == 100  # Menguji sapaan "yo"


