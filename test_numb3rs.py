from numb3rs import validate

def test1():

    assert validate("512.512.1000.1000") == False  # Semua oktet di luar rentang 0-255
    assert validate("1.2.3.4") == True              # Alamat IP valid
    assert validate("1.2.3") == False               # Kurang dari 4 oktet
    assert validate("1.2") == False                 # Kurang dari 4 oktet
    assert validate("1") == False                   # Kurang dari 4 oktet

def test2():

    assert validate("250.75.36.55") == True  # Alamat IP valid

def test3():

    assert validate("255.256.257.258") == False  # Semua oktet di luar rentang 0-255
    assert validate("255.256.255.255") == False  # Oktet kedua di luar rentang
    assert validate("255.255.256.255") == False  # Oktet ketiga di luar rentang
    assert validate("255.255.255.256") == False  # Oktet keempat di luar rentang
