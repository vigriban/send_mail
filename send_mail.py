import smtplib

def get_mail_text_from_template(mail_text, replace_dict):
    for pattern in replace_dict:
        mail_text = mail_text.replace(pattern, replace_dict[pattern])
    return mail_text


def get_recipients_from_file(file_name):
    recipients = []
    with open(file_name, 'r') as f:
        for line in f:
            name, email = line.split(" ")
            recipients.append({"name": name, "email": email.rstrip()})
    return recipients


def send_mails(server, sender_email, template, recipients):
    replace_dict = {
        "%website%": "http://www.dvmn.org",
        "%my_name%": "Виталян",
        "%sender_mail%": sender_email,
    }
    for recipient in recipients:
        replace_dict["%receiver_mail%"] = recipient["email"]
        replace_dict["%friend_name%"] = recipient["name"]
        mail_text = get_mail_text_from_template(template, replace_dict)
        server.sendmail(sender_email, recipient["email"], mail_text.encode("UTF-8"))


if __name__ == '__main__':
    sender_email = "param.pampam1@yandex.ru"
    sender_password = "dbnfkbr83"
    recipients = get_recipients_from_file("friends.txt")
    with open('mail.txt', 'r') as f:
        mail_template = f.read()
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(sender_email, sender_password)
    send_mails(server, sender_email, mail_template, recipients)
    server.quit()