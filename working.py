import re

def main():
    """
    Fungsi utama yang menangani input/output program.
    Meminta pengguna untuk memasukkan rentang waktu dalam format 12 jam dan mencetak hasil konversi ke format 24 jam.
    """
    print(convert(input("Hours: ")))


def convert(s):
    """
    Mengonversi rentang waktu dari format 12 jam ke format 24 jam.

    Parameter:
    s (str): String yang berisi rentang waktu dalam format 12 jam.

    Return:
    str: Rentang waktu dalam format 24 jam.

    Proses:
    1. Memeriksa apakah string sesuai dengan format yang benar menggunakan regex.
    2. Mengambil komponen waktu dari string yang valid.
    3. Mengonversi waktu ke format 24 jam menggunakan fungsi new_format().
    """
    # Memeriksa format waktu menggunakan regex
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)

    if isCorrectFormat:
        pieces = isCorrectFormat.groups()
        # Memeriksa apakah jam berada dalam rentang yang valid
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError("Hour must be between 1 and 12.")

        # Mengonversi waktu ke format 24 jam
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])

        return first_time + ' to ' + second_time
    else:
        raise ValueError("Invalid time format.")


def new_format(hour, minute, am_pm):
    """
    Mengonversi waktu dari format 12 jam ke format 24 jam.

    Parameter:
    hour (str): Jam dalam format 12 jam.
    minute (str): Menit dalam format 12 jam (opsional).
    am_pm (str): Indikator AM atau PM.

    Return:
    str: Waktu dalam format 24 jam.

    Proses:
    1. Mengonversi jam berdasarkan AM/PM.
    2. Menangani kasus khusus untuk jam 12.
    3. Mengembalikan waktu dalam format 24 jam dengan dua digit.
    """
    # Mengonversi jam berdasarkan AM/PM
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12  # 12 PM tetap 12
        else:
            new_hour = int(hour) + 12  # Tambah 12 untuk PM
    else:
        if int(hour) == 12:
            new_hour = 0  # 12 AM menjadi 0
        else:
            new_hour = int(hour)  # Jam tetap sama untuk AM

    # Menangani menit
    if minute == None:
        new_minute = ':00'  # Jika menit tidak diberikan, set ke 00
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute  # Format waktu dengan menit

    return new_time

if __name__ == "__main__":
    main()
