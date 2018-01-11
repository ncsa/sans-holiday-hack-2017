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

punchcard.php:
	wget -O punchcard.php https://gist.githubusercontent.com/Pozo/1004284/raw/fa449480786be7af5e814e63e2a5a66e83d14aef/gistfile1.php
