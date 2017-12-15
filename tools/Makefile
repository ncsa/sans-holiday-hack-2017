all: setup infractions.json infractions_one_per_line.json
setup:
	python3 -m pip install --user -r requirements.txt	
infractions.json: nppd.py
	./nppd.py
infractions_one_per_line.json: infractions.json
	cat infractions.json | jq '.[]' -c > infractions_one_per_line.json
