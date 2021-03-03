def send(msg, conn, format="utf-8"):
    conn.send(msg.encode(format))