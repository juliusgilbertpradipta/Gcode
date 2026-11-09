import pytest  # Mengimpor pytest untuk melakukan pengujian
from fuel import convert, gauge  # Mengimpor fungsi convert dan gauge dari modul fuel

def test_convert():
    assert convert("1/4") == 25  # Menguji konversi 1/4 menjadi 25%
    assert convert("2/4") == 50  # Menguji konversi 2/4 menjadi 50%
    assert convert("3/4") == 75  # Menguji konversi 3/4 menjadi 75%
    assert convert("0/100") == 0  # Menguji konversi 0/100 menjadi 0%
    assert convert("100/100") == 100  # Menguji konversi 100/100 menjadi 100%

    # Menguji pengecualian untuk pembagian dengan nol
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Harus menghasilkan ZeroDivisionError

    # Menguji pengecualian untuk fraksi yang tidak valid
    with pytest.raises(ValueError):
        convert("5/3")  # Harus menghasilkan ValueError (lebih dari 100%)
    with pytest.raises(ValueError):
        convert("abc/3")  # Harus menghasilkan ValueError (input tidak valid)
    with pytest.raises(ValueError):
        convert("-1/4")  # Harus menghasilkan ValueError (bilangan negatif)
    with pytest.raises(ValueError):
        convert("1/-4")  # Harus menghasilkan ValueError (bilangan negatif)

def test_gauge():
    assert gauge(1) == "E"  # Menguji status untuk 1% (harus "E")
    assert gauge(0) == "E"  # Menguji status untuk 0% (harus "E")
    assert gauge(99) == "F"  # Menguji status untuk 99% (harus "F")
    assert gauge(100) == "F"  # Menguji status untuk 100% (harus "F")
    assert gauge(50) == "50%"  # Menguji status untuk 50% (harus "50%")

