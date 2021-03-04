import socket

working = True
while working:
    ADRESS = input("IP>>> ")
    if ADRESS.__contains__(":"):
        working = False
    else:
        print("Please use IP:PORT")


HEADER = 64
PORT = int(ADRESS.split(":")[1])
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"
SERVER = ADRESS.split(":")[0]
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

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