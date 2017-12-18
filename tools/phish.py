#!/usr/bin/env python3
from ewa import EWA

def phish():
    f = "jessica.claus@northpolechristmastown.com"
    to = "alabaster.snowball@northpolechristmastown.com"
    subject = "gingerbread cookie recipe"

    body = "hello!"

    m = EWA()
    resp = m.send_mail(f, to, subject, body)
    print(resp)

if __name__ == "__main__":
    phish()
