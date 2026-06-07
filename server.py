import socket
import threading


HEADER= 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    def recv_exact(conn, n):
        data = b''
        while len(data) < n:
            packet = conn.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data

    connected = True
    while connected:
        header_bytes = recv_exact(conn, HEADER)
        if not header_bytes:
            # client closed connection
            break

        try:
            msg_len = int(header_bytes.decode(FORMAT).strip())
        except ValueError:
            # malformed header
            print(f"[{addr}] Invalid header received: {header_bytes!r}")
            break

        if msg_len == 0:
            continue

        msg_bytes = recv_exact(conn, msg_len)
        if not msg_bytes:
            # client closed before full message
            break

        msg = msg_bytes.decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server is starting...")
start()