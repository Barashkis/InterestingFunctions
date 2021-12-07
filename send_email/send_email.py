import smtplib
import os
import time
import mimetypes
from tqdm import tqdm
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase


def send_email():
    try:
        sender = input("Адрес Вашей электронной почты: ")
        password = input("Пароль: ")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)

        destination = input("Адрес получателя: ")
        template = input("Адрес html шаблона письма: ")

        try:
            with open(template) as file:
                template = file.read()
        except IOError:
            template = None

        msg = MIMEMultipart()
        subject, message = input("Тема письма: "), input("Содержимое письма: ")
        msg["From"] = sender
        msg["To"] = destination
        msg["Subject"] = subject

        if message:
            msg.attach(MIMEText(message))

        if template:
            msg.attach(MIMEText(template, "html"))

        print("Собираю все компоненты письма...")
        time.sleep(0.5)

        for file in tqdm(os.listdir("attachments")):
            time.sleep(0.5)
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)
            file_type, subtype = ftype.split("/")

            if file_type == "text":
                with open(f"attachments/{file}") as f:
                    file = MIMEText(f.read())
            elif file_type == "image":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEImage(f.read(), subtype)
            elif file_type == "audio":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEAudio(f.read(), subtype)
            elif file_type == "application":
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEApplication(f.read(), subtype)
            else:
                with open(f"attachments/{file}", "rb") as f:
                    file = MIMEBase(file_type, subtype)
                    file.set_payload(f.read())
                    encoders.encode_base64(file)

            file.add_header('content-disposition', 'attachment', filename=filename)
            msg.attach(file)

        print("Отправляю письмо...")
        server.sendmail(sender, destination, msg.as_string())

        print("Сообщение было отправлено успешно!")
    except Exception:
        print("Проверьте введенный Вами пароль или логин!")


def main():
    send_email()


if __name__ == "__main__":
    main()
