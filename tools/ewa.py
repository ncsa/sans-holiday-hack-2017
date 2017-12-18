#!/usr/bin/env python3
import binascii
import requests
import sys
import json

PROXY = "socks5h://localhost:32080"

class EWA:
    def __init__(self, host='http://mail.northpolechristmastown.com'):
        self.host = host
        ses = requests.session()
        ses.proxies = {
            "http": PROXY,
        }
        self.ses = ses

    def make_cookies(self, username):
        if '@' not in username:
            username = "{}@northpolechristmastown.com".format(username)
        cookies = {'EWA': json.dumps({
            'name': username,
            'plaintext': '',
            'ciphertext': 'aaaaaaaaaaaaaaaaaaaaaa',
        })}
        return cookies

    def getmail(self, username):
        cookies = self.make_cookies(username)
        resp = self.ses.post(self.host + "/api.js",
            data={"getmail": "getmail"},
            cookies=cookies,
        )
        resp.raise_for_status()
        return resp.json()

    def send_mail(self, from_email, to_email, subject, message):
        message = binascii.hexlify(message.encode('utf-8'))

        cookies = self.make_cookies(from_email)
        resp = self.ses.post(self.host + "/api.js",
            data={
                "from_email": from_email,
                "to_email": to_email,
                "subject_email": subject,
                "message_email": message,
            },
            cookies=cookies,
        )
        resp.raise_for_status()
        return resp.json()
    

if __name__ == "__main__":
    username = sys.argv[1]
    m = EWA()
    mail = m.getmail(username)
    print(json.dumps(mail, indent=True))
