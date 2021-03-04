import socket 
import threading
import json
from connections import send

HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
PASSWORD = "gamer"
DISCONNECT_MESSAGE = "exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def generate(number=10, string=" "):
    product = ""
    for i in range(number):
        product = (product+string)

def run_cmd(cmd):
    if cmd.split()[0]=="help":
        with open("data/help.txt") as f:
            return str(f.read())
    elif cmd.split()[0]=="about":
        with open("data/about.txt") as f:
            return str(f.read())
    elif cmd.split()[0]=="secret":
        product = ""
        with open("secrets.json") as f:
            json_data = json.load(f)
        for i in json_data:
            product += f"\n{i['name']}{generate(10-len(i['name']))}| {i['date']}"

def handle_server():
    while True:
        print(run_cmd(input("")))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    sudo = False
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                send("You have been exited from AIR", conn)

            print(f"[{addr}] {msg}")
            if connected==True:
                if sudo==False and not msg.split()[0]=="sudo":
                    send('You cannot access any data, to do so please do "sudo {password}"', conn)
                elif msg.split()[0]=="sudo":
                    if len(msg.split())==2:
                        if msg.split()[1]==PASSWORD:
                            sudo = True
                            send("[AUTH] You are now in AIR", conn)
                        else:
                            send("[AUTH] Wrong password, deleting thread", conn)
                            connected = False
                    else: send("[SUDO] SYNTAX: sudo {password}", conn)
                else:
                    send(run_cmd(msg), conn)
            else:
                print(f"[DISCONECT] {addr} disconected")
            

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

server_term = threading.Thread(target=handle_server)
server_term.start()

print("[STARTING] server is starting...")
start()