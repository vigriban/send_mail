PATTERN = "%website%"
URL = "http://www.dvmn.org"


def get_mail_with_url(mail_text, pattern, url):
    return mail_text.replace(pattern, url)

    
if __name__ == '__main__':
    with open('mail.txt', 'r') as f:
        mail_data = f.read()
    print(get_mail_with_url(mail_data, PATTERN, URL))

