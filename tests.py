import unittest

import send_mail


class TestSendMail(unittest.TestCase):
    def test_mali_contains_url(self):
        replace_dict = {"%website%": "http://www.dvmn.org", "%name%": "Some name"}
        mail_text = "Please register -> %website%. Your friend, %name%"
        mail_replace = send_mail.get_mail_text_from_template(mail_text, replace_dict)
        for value in replace_dict.values():
            self.assertIn(value, mail_replace)


if __name__ == "__main__":
    unittest.main()
