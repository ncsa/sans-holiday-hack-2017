all: mail.text hints.txt
mail.text: mail.json
	cat mail.json | jq '.INBOX[].BODY.body' -r > mail.text

hints.txt: ../output/tokens.json
	../tools/show_hints.py ../output/tokens.json > hints.txt
