from cryptography.fernet import Fernet


with open('key.key') as f:
    KEY = f.read()
f = Fernet(KEY)

def send(msg, conn, format="utf-8"):
    if msg!=None:
        conn.send(f.encrypt(msg.encode()))
    else:
        conn.send(f.encrypt("Error!".encode()))

def send_raw(binary, conn):
    conn.send(binary)