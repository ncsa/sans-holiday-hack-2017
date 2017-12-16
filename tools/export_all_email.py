#!/usr/bin/env python3
import json
import os
import sys

import ewa

mail_client = ewa.EWA()

db_fn = sys.argv[1]
with open(db_fn) as dbf:
    db = json.load(dbf)

if not os.path.exists("mail"):
    os.mkdir("mail")

for r in db:
    dn, rec = r[0]
    if 'mail' not in rec:
        continue
    email = rec['mail'][0]
    filename = "mail/{}.json".format(email)
    if os.path.exists(filename):
        print("Exists:", filename)
        continue
    print("Downloading:", filename)
    inbox = mail_client.getmail(email)
    with open(filename, 'w') as f:
        f.write(inbox, indent=True)
