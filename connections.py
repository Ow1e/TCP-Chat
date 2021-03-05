from cryptography.fernet import Fernet


with open('key.key') as f:
    KEY = f.read()
f = Fernet(KEY)

def send(msg, conn, format="utf-8"):
    conn.send(msg.encode(format))

def send_raw(binary, conn):
    conn.send(binary)