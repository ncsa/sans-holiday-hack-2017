import jwt
import tqdm

words = [w.strip() for w in open("/usr/share/dict/words")]

#cookie='xj6oYqq87s996e536780'
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTA4LTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.M7Z4I3CtrWt4SGwfg7mi6V9_4raZE5ehVkI9h04kr6I'

for w in tqdm.tqdm(words):
    try:
        v = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(w, v)
    except jwt.exceptions.DecodeError:
        pass
