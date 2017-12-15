all: mail.text hints.md
mail.text: mail.json
	cat mail.json | jq '.INBOX[].BODY.body' -r > mail.text

hints.md: ../output/tokens.json ../tools/show_hints.py
	../tools/show_hints.py ../output/tokens.json > hints.md
