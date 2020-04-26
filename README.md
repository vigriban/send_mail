# Send mail

Send emails about devman programming course to list of friends

## Getting Started

Clone repository to separate directory, install dependencies, list your friends in `friends.txt`,
indicate your email info in `.env`, run script.
Example: 
```bash
echo "Vasya vasya1@mail.ru" >> friends.txt
echo "EMAIL_ADDRESS=m@mail.ru" >> .env
echo "EMAIL_PASSWORD=password" >> .env
echo "SMTP_HOST=smtp.yandex.ru:465" >> .env
python3 send-mail.py
```

### Prerequisites

```
python3
pip3
```

### Installing
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
## Running the tests

```bash
python3 tests.py
```

## License

This project is licensed under the MIT License.
