import requests
from multiprocessing import Pool


def test_request(url, retry=5):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    try:
        requests.get(url=url, headers=headers)
    except Exception:
        if retry:
            return test_request(url, retry=(retry - 1))
        else:
            return url
    else:
        return


def main():
    failed_urls = []

    while True:
        try:
            fname = input("Введите путь к текстовому файлу, который содержит ссылки, соединение с которыми "
                          "нужно проверить: ")

            with open(f"{fname}.txt") as file:
                urls = file.read().strip().splitlines()
        except Exception:
            print("Что-то пошло не так... Введите правильный путь к файлу.")
        else:
            print("Программа анализирует ссылки...")
            break

    with Pool(10) as p:
        for url in p.imap_unordered(test_request, urls):
            if url:
                failed_urls.append(url)

    with open("log.txt", "w") as file:
        file.write("\n".join(failed_urls))

    print("Работа завершена.")


if __name__ == "__main__":
    main()
