import re

def main():

    print(parse(input("HTML: ")))

def parse(s):

    # Memeriksa keberadaan tag iframe dalam HTML
    if re.search(r"<iframe(.)*><\/iframe", s):
        # Mencari pola URL YouTube embed dalam iframe
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)(\w+)", s)

        if url_pattern:
            # Split URL menjadi komponen-komponennya
            split_url = url_pattern.groups()
            # Membentuk ulang URL dalam format singkat youtu.be
            return "https://youtu.be/" + split_url[3]

    # Mengembalikan None jika tidak menemukan iframe YouTube yang valid
    return None

if __name__ == "__main__":
    main()
