import socket
import os
import sys
from cryptography.fernet import Fernet

clear_cmd = 'clear'
working = True
while working:
    ADRESS = input("IP>>> ")
    if ADRESS.__contains__(":"):
        working = False
    else:
        print("Please use IP:PORT")

with open('messages.log', 'w') as f:
    f.write("")

HEADER = 64
PORT = int(ADRESS.split(":")[1])
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"
SERVER = ADRESS.split(":")[0]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def encrypt(binary, key):
    f = Fernet(key)
    return f.encrypt(binary)

def decrypt(binary, key):
    f = Fernet(key)
    return f.decrypt(binary)

def key():
    if os.path.exists('key.key'):
        with open('key.key') as f:
            return f.read()
    else:
        sys.exit("No key found!")

KEY = key()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    message = (decrypt(client.recv(2048), KEY).decode(FORMAT))
    with open("messages.log", "a") as f:
        if message!="$Update$":
            f.write(message+"\n")
            os.system(clear_cmd)
    with open('messages.log') as f:
        print(f.read())

    

working = True
send("$Welcome$")
while working:
    cmd = input(">>> ")
    if cmd=="exit":
        print("Exiting...")
        send(cmd)
        working = False
    else:
        send(cmd)