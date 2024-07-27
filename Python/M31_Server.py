#python -m http.server (8000)//this is optional but you can change the port
#http://localhost:8000

#python -m http.server --bind 192.168.0.25 //-b will work instead of --bind
#http://192.168.0.25:8000/

#These are the ways of creating a server using cmd

import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.0.25"
SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the IPV4, so unlike the line above, will work in the other computers
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"{addr} has connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"{addr}: {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
            conn.send("Msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

print("Server is starting.")
start()
