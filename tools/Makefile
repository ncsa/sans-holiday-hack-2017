all: setup cve_2017_9805.py jwt2john.py pw.py
setup:
	python3 -m pip install --user -r requirements.txt	

cve-2017-9805.py:
	wget https://raw.githubusercontent.com/chrisjd20/cve-2017-9805.py/master/cve-2017-9805.py
cve_2017_9805.py: cve-2017-9805.py
	ln -sf cve-2017-9805.py cve_2017_9805.py

jwt2john.py:
	wget https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py

pw.py:
	wget https://raw.githubusercontent.com/s4y/pw/master/pw.py
