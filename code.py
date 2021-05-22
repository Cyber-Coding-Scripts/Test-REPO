import os as term
import subprocess
import platform
import socket
import random
import string
import time

term.system('title ' + 'Cyber-Terminal')
path = 'C:/'
path2 = 'E:/'
path3 = 'D:/'
quit = "/h"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
chars_e = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!0123456789'

print("""Kinect | Cyber Terminal [Version 1.00]
(C) Kinect Software. All rights reserved.
	""")

def main():
	while True:
		command = input("@" + host_name + "> ")

		if command == '/t':
			print("Opening " + platform.system() + " " + platform.release() + " Terminal...")
			time.sleep(0.5)
			terminal()

		if command == 'ping':
			ping_s()

		if command == 'local':
			local()

		if command == 'help':
			help()

		if command == 'cls':
			break

		if command == 'net list':
			net()

		if command == 'password':
			password()

		if command == 'title':
			title()

		if command == 'os':
			os()

		if command == 'info':
			license()

def terminal():
	while True:
		command2 = input("@" + host_name + "/>> ")

		if command2 == quit:
			print("Opening Home Terminal...")
			time.sleep(0.5)
			main()
		else:
			term.system(command2)

def ping_s():
	host = input("Enter Website To Ping: ")
	number = input("Enter How Many Times To Ping: ")

	def ping(host):
		param = '-n' if platform.system().lower() == 'windows' else '-c'
		run = ['ping', param, number, host]
		return subprocess.call(run)
	print(ping(host))

def local():
	print("Your Local IPS Is: " + host_ip)

def password():
    number_e = input('Please Enter a Number of Passwords to Genirate: ')

    try:
    	number_e = int(number_e)
    except:
    	print("Error, please enter a number!")

    length_e = input('Enter how Many Chacaters To a Generate: ')
    try:
    	length_e = int(length_e)
    except:
    	print("Error, please enter a number!")
    print('\nHere are your password(s): ')

    for pwd_e in range(number_e):
    	password_e = ''
    	for c in range(length_e):
    		password_e += random.choice(chars_e)
    	print(password_e)

def net():
	print("Finding All Active Connections")
	time.sleep(0.5)
	term.system('netstat')

def title():
	name = input("Enter new title Name: ")
	time.sleep(0.5)
	term.system('title ' + name)
	print("title Changed Successfully To: " +  name)

def os():
	print("OS NAME: " + platform.system())
	print("OS VERSION: " + platform.release())

def license():
	print("Company Name: Kinect Software")
	print("ever since: 2020-2021")
	print("Version Update: 1.00")
	print("Website: https://kinectcode.com/")
	print("Contact Email: kinectcode@gmail.com")
	print("""About: Kinect Software Was Founded in 2020  By Aidan Bologna,
Kinect's Main Goal Is To Make Software Easy To Use.
That's Why We Made The Cyber-Terminal a Super Easy To-Use Terminal""")

def help():
	print("""
[/t] Switch into terminal commands
[ping] Ping any website
[net list] List all the Curennt Active Network Connections
[password] Genirate random passwords
[local] list your local IPS
[title] Change the title name of the terminal
[close] Close the terminal
[os] List Your OS Name And Version Update
[help] list all commands for Cyber-Terminal
	""")

main()
