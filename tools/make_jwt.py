import sys
import jwt

SECRET_KEY='3lv3s'

user = sys.argv[1]
dept = sys.argv[2]
ou = sys.argv[3]

data = {
    'dept': dept,
    'ou': ou,
    'uid': user,
    'expires': '2018-08-16 12:00:47.248093+00:00',
}

token = jwt.encode(data, key=SECRET_KEY)
print(token.decode('utf-8'))
