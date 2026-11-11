from um import count

def main():
    
    test_upper_lower_case()     # Test untuk case sensitivity
    test_word_with_um()         # Test untuk kata yang mengandung 'um'
    test_surrounded_by_space()  # Test untuk spasi dan tanda baca

def test_upper_lower_case():

    assert count('Um, thanks for the album.') == 1  # Menguji 1x muncul dengan huruf besar
    assert count('Um, thanks, um...') == 2         # Menguji 2x muncul dengan case berbeda

def test_word_with_um():

    assert count('yummi') == 0  # Mengecek false positive pada kata mengandung 'um'

def test_surrounded_by_space():

    assert count('Hello, um, world') == 1  # 'um' di antara koma dan spasi
    assert count('um?') == 1               # 'um' diikuti tanda tanya

if __name__ == "__main__":

    main()
