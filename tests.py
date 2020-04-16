import unittest

import send_mail


class TestSendMail(unittest.TestCase):
    def test_mali_contains_url(self):
        pattern = "%website%"
        mail_text = "Please register -> %website%"
        url = "http://www.dvmn.org"
        mail_for_send = send_mail.get_mail_with_url(mail_text, pattern, url)
        self.assertIn(url, mail_for_send)


if __name__ == "__main__":
    unittest.main()
