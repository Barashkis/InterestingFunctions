import smtplib
from email.mime.text import MIMEText


def send_email():
    sender = input("Введите адрес своей электронной почты: ")
    password = input("Введите пароль: ")
    destination = input("Введите адрес получателя: ")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        message, subject = input("Содержимое письма: "), input("Тема письма: ")
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(sender, destination, msg.as_string())

        print("Письмо отправлено успешно!")
    except Exception as ex:
        print(f"Проверьте логин и пароль, пожалуйста.")


def main():
    send_email()


if __name__ == "__main__":
    main()
