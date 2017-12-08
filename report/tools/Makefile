all: setup infractions.json
setup:
	python3 -m pip install --user -r requirements.txt	
infractions.json: nppd.py
	./nppd.py
