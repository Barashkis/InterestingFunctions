import datetime

import img2pdf
import os
from pathlib import Path


def convert_to_pdf():
    """
    Функция, которая объединяет все .jpg картинки в текущей дериктории
    (то есть там же, где расположен скрипт)
    """
    img_list = []

    for file_name in os.listdir():
        if not file_name.endswith(".jpg"):
            continue
        path = str(Path(file_name))
        if os.path.isdir(path):
            continue
        img_list.append(path)

    if img_list:
        with open(f"{datetime.datetime.now().strftime('%d_%m_%Y')}.pdf", "wb") as f:
            f.write(img2pdf.convert(img_list))


def main():
    convert_to_pdf()


if __name__ == "__main__":
    main()
