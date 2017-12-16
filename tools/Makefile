all: setup infractions.json infractions_one_per_line.json jwt.john
setup:
	python3 -m pip install --user -r requirements.txt	
infractions.json: nppd.py
	./nppd.py
infractions_one_per_line.json: infractions.json
	cat infractions.json | jq '.[]' -c > infractions_one_per_line.json

jwt2john.py:
	wget https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py

jwt.john: jwt2john.py jwt
	python3 jwt2john.py $(shell cat jwt) > jwt.john
