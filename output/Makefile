all: mail.text hints.md alabaster.jwt santa.jwt
mail.text: mail.json
	cat mail.json | jq '.INBOX[].BODY.body' -r > mail.text

hints.md: ../output/tokens.json ../tools/show_hints.py
	../tools/show_hints.py ../output/tokens.json > hints.md

alabaster.jwt:
	python3 ../tools/make_jwt.py alabaster.snowball Engineering elf > alabaster.jwt

santa.jwt:
	python3 ../tools/make_jwt.py santa.claus administrators human > santa.jwt
