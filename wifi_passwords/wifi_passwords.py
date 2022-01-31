import subprocess


def get_passwords():
    profiles_data = subprocess.check_output("netsh wlan show profiles", encoding="CP866").split("\n")
    profiles = [i.split(":")[1].strip() for i in profiles_data if "Все профили пользователей" in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f"netsh wlan show profile {profile} key=clear", encoding="CP866").split("\n")

        try:
            password = [i.split(":")[1].strip() for i in profile_info if "Содержимое ключа" in i][0]
        except IndexError:
            password = "пароль отсутствует"

        with open("passwords.txt", "a+", encoding="utf-8") as file:
            file.write(f"Пароль от {profile}: {password}\n\n{'-' * 20}\n\n")


def main():
    get_passwords()


if __name__ == '__main__':
    main()
