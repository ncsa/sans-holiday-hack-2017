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

    def upload(self, username, filename):
        files = {'file': open(filename, 'rb')}

        cookies = self.make_cookies(username)
        resp = self.ses.post(self.host + "/upload", cookies=cookies, files=files)
        body = resp.text
        #body looks like like:
        #<html><h1 style="text-align: center;">File Uploaded and link Attached!</h1><script>window.setTimeout(function() {window.location.href = '/upload.js'}, 2000);</script><script>localStorage.setItem("file_link", "http://mail.northpolechristmastown.com/attachments/DaM5HE08t7cynFqztM0a4VcVg8CBU2Gs7HprLQWzsdnSCRuj5L__cookies.docx");</script></html>
        #extract the link.  The link is the one string between quotes that contains http
        links = [frag for frag in body.split('"') if 'http' in frag]
        return links[0]

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
